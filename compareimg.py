#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:47:45 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np
import os

original = cv2.imread("/bmiit/stud/202006100110116/Desktop/i.png")
img_to_comper = cv2.imread("/bmiit/stud/202006100110116/Desktop/i.png") 

#cv2.imshow("dif",dif)


os.system("clear") 

if original.shape == img_to_comper.shape:
    
    dif = cv2.subtract(original,img_to_comper)
    b,g,r = cv2.split(dif)
    
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("image is same")
        cv2.imshow("original",original)
        cv2.imshow("img_to_comper",img_to_comper)
    else:
        print("image is not same")

original = cv2.resize(original,(100,60))
img_to_comper = cv2.resize(img_to_comper,(100,60))

cv2.waitKey(0)

cv2.destroyAllwindows()