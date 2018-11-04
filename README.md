# ComixGAN

This repo contains code for training ComixGAN. It is trained using COCO dataset and ~1000 comic images obtained by extracting keyframes from some cartoons.


## Steps

1. Prepare third dataset with comic images with blurred edges. Steps:
    - Detect edge pixels using a standard Canny edge detector.
    - Dilate the edge regions. 
    - Apply a Gaussian smoothing in the dilated edge regions.  
         
2. Split dataset to training, validation and testing:
    - Testing: Get 5k of random coco images as final test dataset
    - For point 4: 5k COCO validation images. All the remaining images used for training.
    - For point 5:
        - COCO: 5k validation images. All the remaining images use for training.
        - Comic: 100 validation images.
        - Comic blurred: 100 validation images.
        - All the remaining images are used for training.          
          
3. Training in batches using 384x384 images.
    - Sample images in batches   
4. Pretrain Generator to make it return output the same with the input (On whole COCO dataset).
5. Pretrain Discriminator on COCO and comic images.
6. Adversarial Training and tuning of D and G:
    - Loss that consists of Adversarial Loss (including smoothed edges part) + Content Loss with weight=10 
7. Test on 5k final test dataset.
8. Add Callbacks (Weights saving [x], history saving [x])

## Changes in comparison with CartoonGAN:
- Non-saturating loss for Generator
- Generator/Discriminator ration during adversarial training: 3:1 (3 G weights updates for 1 D update) 
- Pretrained discriminator
- Sigmoid in last D layer

## Sample results

![alt text](https://github.com/maciej3031/comixGAN/blob/master/examples/example1.png)
![alt text](https://github.com/maciej3031/comixGAN/blob/master/examples/example2.png)
![alt text](https://github.com/maciej3031/comixGAN/blob/master/examples/example3.png)

