# Fine-Tune VGG-Face weight
This is my experiment to fine-tune VGG-Face weight to make it recognizes faces on custom dataset

Two questions to answer:
  1. How well VGG-Face recognizes face that are not present in its pre-trained model after modifying and retraining only the last layers?
  2. How many layers need to be trained to gain the best classification result?

The structure of the folder is same as other CNN classification where we have train, validation and test folders.

![Alt text](https://github.com/RezaPurut/Deep_Learning_experiment/blob/master/fine_tune_vggface/structure.png)

Three celebrities were selected (*TWICE members*) and all of their images were downloaded from google. Their images also have been cropped using OpenCV before splitted into train, validation and test.

I refer this link https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751 to guide me do the fine-tuning

![Alt text](https://github.com/RezaPurut/Deep_Learning_experiment/blob/master/fine_tune_vggface/decision_map.png)
<p align="center"><i>(Marcelino, 2018)</i></p>

Quadrant 3 and 4 were selected in this experiment. Why?
Because we have small dataset

# What I Learned
- Before I proceed with 10 images per class in training folder, I use 5 images per class for training and 3 images per class for validation but the classification is quite sucks. Then, I decided to add 5 more images into training folder and 3 more images in validation folder
- I noticed that increasing the number of epochs could lead to a much better accuracy, validation accuracy, lower loss and validation loss but it is important to watch out for overfitting and underfitting
- VGG-Face can be used to recognizes face by only training the last layers and also retraining some of the layers (in my case freezing 0-9 layers and retraining the remaining layers give the best result)

## Inspiration
Got inspiration from this guy project btw -> https://github.com/curaai00/my-twice-cnn

## References
https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751

https://github.com/skylarhuang/ML_Intro_project/blob/master/Fine_Tuning_Vgg_Face.ipynb

https://github.com/serengil/tensorflow-101/blob/master/python/vgg-face.ipynb

https://github.com/llSourcell/how_to_make_an_image_classifier/blob/master/demo.ipynb
