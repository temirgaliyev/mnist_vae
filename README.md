# mnist_vae
Variational Autoencoder using MNIST dataset  
[Colab Demo](https://colab.research.google.com/drive/1WpfOQZxpkq-eL7eT5kWvJvKTzxKJAww-)  

[Examples](#examples)  
[Description](#description)  
[TODO](#todo)  
[Links](#links)

## Examples  
| ![Exploring Latent Space gif](https://github.com/temirgaliyev/mnist_vae/blob/master/static/example.gif) | 
|:--:| 
| *Exploring Latent Space* |

| ![Some examples from test set](https://github.com/temirgaliyev/mnist_vae/blob/master/static/example.png) | 
|:--:| 
| *Some examples from test set* |

## Description
Another one Variational Autoencoder trained on MNIST

## TODO
- [x] Create VAE training pipeline and train
- [ ] Architecture
  - [x] BCE loss instead of MSE
  - [x] Convolutional Pooling instead of MaxPool
  - [ ] Train Autoencoder
  - [ ] Train Fully-Coonvolutional AE
  - [ ] Train Variational Autoencoder
  - [x] Train Fully-Coonvolutional VAE
- [ ] Compare different architectures (Need some metric)
- [x] Minimum working example in Colab
- [ ] Train VAE on different dataset (ex. [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html ))  
  
## Links
[Github: Pytorch Examples](https://github.com/pytorch/examples)  
[Arxiv: Auto-Encoding Variational Bayes](https://arxiv.org/pdf/1312.6114.pdf)  
