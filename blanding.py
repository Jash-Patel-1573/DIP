#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:20:41 2023

@author: bmiit202006100110116
"""

# import OpenCV file
import cv2
import numpy as np

# Read Image1
img1 = cv2.imread('/bmiit/stud/202006100110116/Desktop/i.png', 1)

# Read image2
img2 = cv2.imread('/bmiit/stud/202006100110116/Desktop/download.jpeg', 1)

img1 = cv2.resize(img1,(500,500))

img2 = cv2.resize(img2,(500,500))

brit = np.mean(img1)

# Blending the images with 0.3 and 0.7
img = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
img1 = cv2.addWeighted(img1, 0.7, img2, 0.3,10)

# Show the image
cv2.imshow('image', img)
cv2.imshow('image1', img1)

cv2.imwrite("img.png",img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()
