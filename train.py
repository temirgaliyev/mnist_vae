import torch
from torchvision.utils import save_image

from timeit import default_timer as timer
from os import path

from .models import (
	MaxPoolEncoder, ConvPoolEncoder, Decoder, VAE,
	BCE_KLD_loss, MSE_KLD_loss
	)
from .utils import create_folders, get_dataloader, train, test


def main(epochs=1000, batch_size=1024, cuda=True, loss_bce=True, pool_conv=True):
	print("Initialization...")
	WEIGHT_FILENAME_PREFIX = "WEIGHT_{}_{}_".format(
							'BCE' if loss_bce else 'MSE',
							'CONV' if pool_conv else 'MAXP')
	cuda_available = torch.cuda.is_available()
	device = torch.device("cuda" if cuda_available and cuda else "cpu")
	loss_function = BCE_KLD_loss if loss_bce else MSE_KLD_loss
	encoder_class = ConvPoolEncoder if pool_conv else MaxPoolEncoder

	print("Creating folders...")
	create_folders("data", 
		path.join("results", "rand"), 
		path.join("results", "test"), 
		path.join("results", "weights"))

	print("Loading MNIST...")
	train_loader = get_dataloader("data", True, batch_size)
	test_loader = get_dataloader("data", False, batch_size)

	random_test = torch.randn(64, 16).to(device)

	encoder = encoder_class()
	decoder = Decoder()
	model = VAE(encoder, decoder).to(device)
	optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

	print("Training...")
	train_losses, test_losses = [], []
	for epoch in range(1, epochs+1):

		time_started = timer()

		train_loss = train(epoch, train_loader, model, loss_function, device, optimizer)
		test_loss = test(epoch, test_loader, model, loss_function, device, True)

		time_elapsed = timer() - time_started

		print(f"Epoch: {epoch}/{epochs:02d} | Train loss: {train_loss:02.7f} | Test loss: {test_loss:02.7f} | Time: {time_elapsed}")

		train_losses.append(train_loss)
		test_losses.append(test_loss)

		with torch.no_grad():
			random_sample = model.decoder(random_test).cpu()
			save_image(random_sample, f"results/rand/{epoch:02d}.png")

		if epoch%100 == 0 or epoch == epochs:
			filename = f"{epoch}_{test_loss:02.7f}.torch"
			weight_path = path.join("results", "weights", WEIGHT_FILENAME_PREFIX+filename)
			torch.save(model, weight_path)
			print(f"SAVING weights at {weight_path}")

	print("Completed!")
