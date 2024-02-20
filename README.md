# Projet_IMI

## To change the parameters test :

### The 'test_name' param :
The name of the current test, onve the training is over put it in the test_list in the plotting curve cell (the last one) to print the result of this test. If you made several training with different test_name, add them all to get the result of each test.

### If test = clean :
Add the noise (Gaussian noise) during the training -> better because data augmentation.
The param noise_factor controll the amount of noise (0.5 is already a lot).

### If test = noisy :
The noise (Gaussian noise) is add before the training and the noised images are save in the Database folder next to the non-noised file.
The param noise_factor is no longer used.

### The 'size' param :
It is use to change the size of the images, the more it is the longer the training wil be (6 hours for 512x512 and 1h30 for 256x256 on CPU).

### The 'n' param :
This one is for the number of test image you plot during the training (do not put 0 please).

### The 'epochs' param :
It is the number of time the network is train. Usually 10 epochs is enough with this dataset.

## Sources :

Auto-Encodeur convolutif :
https://plainenglish.io/blog/denoising-autoencoder-in-pytorch-on-mnist-dataset-a76b8824e57e
https://www.youtube.com/watch?v=rGz_NavEMmM&list=PLlI0-qAzf2Sa6agSVFbrrzyfNkU5--6b_&index=10

Couches Convolutives information :
https://inside-machinelearning.com/cnn-couche-de-convolution/#:~:text=%C3%80%20l'inverse%2C%20les%20couches,convolutions%20ont%20une%20approche%20locale.
https://cedric.cnam.fr/vertigo/cours/ml2/coursDeep3.html

Forum (resize & range) :
https://discuss.pytorch.org/t/does-pytorch-automatically-normalizes-image-to-0-1/40022
https://discuss.pytorch.org/t/how-to-efficiently-normalize-a-batch-of-tensor-to-0-1/65122
https://stackoverflow.com/questions/72440228/how-to-rescale-a-pytorch-tensor-to-interval-0-1
https://stackoverflow.com/questions/76419715/will-torchvision-transforms-resize-damage-the-image-information

Bruit IRM images :
https://www.imaios.com/fr/e-mri/qualite-d-image-et-artefacts/rapport-signal-et-bruit