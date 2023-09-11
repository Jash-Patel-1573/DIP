#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:41:08 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np


img = cv2.imread("4.jpg",1)
gamma =0.5

new = np.array(255 * (img/255)**gamma).astype("uint8")


cv2.imshow("image",img)
cv2.imshow("image4.jpg",new)
cv2.imwrite("image4.jpg",new)

cv2.waitKey(0)

cv2.destroyAllWindows()