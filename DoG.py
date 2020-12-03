#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:22:38 2020

@author: rajiv
"""


import numpy as np
from skimage.filters import difference_of_gaussians
from PIL import Image


def DoG(image_name, Test= False):
    train_path = "/home/rajiv/Documents/lectures/BIC/project_conv_sdnn/datasets/TrainingSet/Face/"
    test_path = "/home/rajiv/Documents/lectures/BIC/project_conv_sdnn/datasets/TestingSet/Face/"
    image = np.asarray(Image.open(train_path+image_name))
    image = image[34:434, 154:554]
    filtered_image = difference_of_gaussians(image, 1.5)
    filtered_image = np.expand_dims(filtered_image, axis = 0)
    filtered_image = np.expand_dims(filtered_image, axis = 0)
    return filtered_image
    