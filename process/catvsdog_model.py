from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from matplotlib.image import imread
from process.reshape_dataset import reshape_data
from numpy import load

from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random

from process.vgg3 import run_test_harness
from process.final_dataset import final_dataset


class LoadData:
	def __init__(self):
		self.load_dog_data()
		self.load_cat_data()

	def load_dog_data(self):
		# define location of dataset
		folder = 'D:\\UDAY\\ML_API\\train\\'
		# plot first few images
		for i in range(9):
			# define subplot
			pyplot.subplot(330 + 1 + i)
			# define filename
			filename = folder + 'dog.' + str(i) + '.jpg'
			# load image pixels
			image = imread(filename)
			# plot raw pixel data
			pyplot.imshow(image)
		# show the figure
		pyplot.show()

	def load_cat_data(self):
		# plot cat photos from the dogs vs cats dataset
		# define location of dataset
		folder = 'D:\\UDAY\\ML_API\\train\\'
		# plot first few images
		for i in range(9):
			# define subplot
			pyplot.subplot(330 + 1 + i)
			# define filename
			filename = folder + 'cat.' + str(i) + '.jpg'
			# load image pixels
			image = imread(filename)
			# plot raw pixel data
			pyplot.imshow(image)
		# show the figure
		pyplot.show()


if __name__ == "__main__":
	# LoadData()
	# reshape_data()
	#
	# photos = load('D:\\UDAY\\ML_API\\dogs_vs_cats_photos.npy')
	# labels = load('D:\\UDAY\\ML_API\\dogs_vs_cats_labels.npy')

	# dataset_home = 'D:\\UDAY\\ML_API\\dataset_dogs_vs_cats\\'
	# subdirs = ['train\\', 'test\\']
	# for subdir in subdirs:
	# 	# create label subdirectories
	# 	labeldirs = ['dogs\\', 'cats\\']
	# 	for labldir in labeldirs:
	# 		newdir = dataset_home + subdir + labldir
	# 		makedirs(newdir, exist_ok=True)
	# # seed random number generator
	# seed(1)
	# # define ratio of pictures to use for validation
	# val_ratio = 0.25
	# # copy training dataset images into subdirectories
	# src_directory = 'D:\\UDAY\\ML_API\\train'
	# for file in listdir(src_directory):
	# 	src = src_directory + '\\' + file
	# 	dst_dir = 'train\\'
	# 	if random() < val_ratio:
	# 		dst_dir = 'test\\'
	# 	if file.startswith('cat'):
	# 		dst = dataset_home + dst_dir + 'cats\\' + file
	# 		copyfile(src, dst)
	# 	elif file.startswith('dog'):
	# 		dst = dataset_home + dst_dir + 'dogs\\' + file
	# 		copyfile(src, dst)
	final_dataset()
	run_test_harness()
