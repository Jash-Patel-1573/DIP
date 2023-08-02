#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:25:44 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np

img = cv2.imread("/bmiit/stud/202006100110116/Desktop/5.jpg")


alpha = 2.0
beta = -180

new = alpha * img + beta
new = np.clip(new, 0, 255).astype(np.uint8)

cv2.imshow("orignal img.", img)

cv2.subtract(new,50)

cv2.imshow("cleaned.png", new)

cv2.waitKey(0)
cv2.destroyAllwindows()