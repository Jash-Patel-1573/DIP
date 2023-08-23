#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:27:22 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np

def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = ((image - min_val) / (max_val - min_val)) * 255
    stretched_image = stretched_image.astype(np.uint8)
    return stretched_image

def adjust_brightness(image, value):
    adjusted_image = cv2.convertScaleAbs(image, alpha=1, beta=value)
    return adjusted_image

image = cv2.imread('new-image.jpg', cv2.IMREAD_GRAYSCALE)

stretched_image = contrast_stretching(image)

brightness_adjusted = adjust_brightness(image, 25)  # Increase brightness by 50


cv2.imshow('Brightness Adjusted Image', brightness_adjusted)
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
