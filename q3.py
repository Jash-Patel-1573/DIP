#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:53:03 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np

img = cv2.imread("3.jpg",1)
img1 = cv2.imread("4.jpg",1)

gamma =0.5

new = np.array(255 * (img/255)**gamma).astype("uint8")
cv2.imshow("image3",img)
cv2.imshow("image4",new)
cv2.imwrite("image3.jpg",new)


new1 = np.array(255 * (img1/255)**gamma).astype("uint8")
cv2.imshow("image",img1)
cv2.imshow("image4.jpg",new1)
cv2.imwrite("image4.jpg",new1)


cv2.waitKey(0)

cv2.destroyAllWindows()