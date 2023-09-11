#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:32:31 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("5.jpg",0)

hist= cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

avg = img.mean()

thresh, binary = cv2.threshold(img, 55, 255, cv2.THRESH_BINARY)
cv2.imshow("55",binary)

thresh1, binary1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("127",binary1)

thresh1, binary2 = cv2.threshold(img, avg, 255, cv2.THRESH_BINARY)
cv2.imshow("avg " + str(avg) ,binary2)

otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("otsu" ,image_result)


cv2.waitKey(0)

cv2.destroyAllWindows()