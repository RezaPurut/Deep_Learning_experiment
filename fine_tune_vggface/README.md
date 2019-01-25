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
<p align="center">*(Marcelino, 2018)*</p>

Quadrant 3 and 4 were selected in this experiment.

## Comments
It is quite confusing actually because I'm not even sure whether my dataset is similar or different from pre-trained model. If I say similar, the dataset (the images) is not in pre-trained model but if I say different, my dataset is face images. That is why I select both Quadrant 3 and 4. It will be great if the author of that website/blog give more detailed explanation.

## Inspiration
Got inspiration from this guy project btw -> https://github.com/curaai00/my-twice-cnn

## References
https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751

https://github.com/skylarhuang/ML_Intro_project/blob/master/Fine_Tuning_Vgg_Face.ipynb

https://github.com/serengil/tensorflow-101/blob/master/python/vgg-face.ipynb

https://github.com/llSourcell/how_to_make_an_image_classifier/blob/master/demo.ipynb
