# Projet_IMI

## To change the parameters test :

### The 'test_name' param :
The name of the current test, onve the training is over put it in the test_list in the plotting curve cell (the last one) to print the result of this test. If you made several training with different test_name, add them all to get the result of each test.

### If test = clean :
Add the noise during the training -> better because data augmentation.
The param noise_factor controll the amount of noise (0.5 is already a lot).

### If test = noisy :
The noise is add before the training and the noised images are save in the Database folder next to the non-noised file.
The param noise_factor is no longer used.

### The 'size' param :
It is use to change the size of the images, the more it is the longer the training wil be (6 hours for 512x512 and 1h30 for 256x256).

### The 'n' param :
This one is for the number of test image you plot during the training (do not put 0).

### The 'epochs' param :
It is the number of time the network is train.