#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:31:08 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


# Read the image
img_noisy1 = cv2.imread('/bmiit/stud/202006100110116/Desktop/116/5.jpg', 1)

kernal = np.ones((5,5),np.float32)/25
kernal1 = np.ones((3,3),np.float32)/9

sfilter = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])

blurred=cv2.filter2D(img_noisy1,-1,kernal1)
blurred1=cv2.filter2D(blurred,-1,sfilter)
blurred2=cv2.filter2D(blurred1,-1,kernal1)
blurred3=cv2.filter2D(blurred2,-1,sfilter)

cv2.imshow("original",img_noisy1)
cv2.imshow("blurred",blurred)
cv2.imshow("blurred1",blurred1)
cv2.imshow("blurred2",blurred2)
cv2.imshow("blurred3",blurred3)

cv2.waitKey(0)
cv2.destroyAllWindows()