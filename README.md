# Caffe-python

In this project, I used Python + a caffe-trained CNN to classify and localize images from a subset of ImageNet. This project is divided into two parts:

1. Image Classification

	In this part, a CNN which takes a 32x32x3 image as input and has 4 output nodes followed by a Softmax layer is designed and trained. 

2. Image Localization

	In this part, some pre and post processing is done in order to localize a class instance in an image. This is implemented in four phases:
	
	Phase 1: Creation of dataset for training
	Phase 2: Preparing train and test splits
	Phase 3: Training
	Phase 4: Testing

	The NN created in Part1 is used in Part2 as well.
	

	


