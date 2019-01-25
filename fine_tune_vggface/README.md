# Fine-Tune VGG-Face weight
This is my experiment to fine-tune VGG-Face weight to make it recognizes faces on custom dataset

Two questions to answer:
  1. How well VGG-Face recognizes face that are not present in its pretrained model after modifying and retraining only the last layers?
  2. How many layers need to be trained to gain the best classification result?

The structure of the folder is same as other CNN classification where we have train, validation and test folders.

![Alt text](https://github.com/RezaPurut/Deep_Learning_experiment/blob/master/fine_tune_vggface/structure.png)

Three celebrities were selected (TWICE members) and all of their images were downloaded from google. Their images also have been cropped using OpenCV before splitted into train, validation and test.

I refer this link https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751 to do the fine-tuning
