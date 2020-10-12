
# # most of our imports
# import warnings
# import numpy as np
# import os
#
# from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
# # %matplotlib inline
# import matplotlib.pyplot as plt
# from art.classifiers import KerasClassifier

from lib.data_utils import *


# Load the raw CIFAR-10 data
cifar10_dir = 'lib/datasets/cifar-10-batches-py'
X_train, y_train, X_test, y_test = load_cifar10(cifar10_dir)

print(X_train.shape)