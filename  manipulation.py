#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 12:56:52 2023

@author: bmiit202006100110116
"""

import cv2
import numpy as np

# Load an image
image_path = "/bmiit/stud/202006100110116/Desktop/i.png"  # Replace with the path to your image
image = cv2.imread(image_path)

# Resize the image
resized_image = cv2.resize(image, (100 , 60))  # Replace new_width and new_height with desired dimensions

# Rotate the image
angle = 45  # Replace with the desired rotation angle in degrees
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# Flip the image
flipped_image_horizontal = cv2.flip(image, 1)  # 1 for horizontal flip
flipped_image_vertical = cv2.flip(image, 0)    # 0 for vertical flip
flipped_image_both = cv2.flip(image, -1)       # -1 for both horizontal and vertical flip

# Apply filters (e.g., Gaussian blur and Canny edge detection)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # (5, 5) is the kernel size, and 0 is the standard deviation
canny_edges = cv2.Canny(image, 100, 200)  # 100 and 200 are the min and max thresholds

# Show the manipulated images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Flipped Horizontal Image", flipped_image_horizontal)
cv2.imshow("Flipped Vertical Image", flipped_image_vertical)
cv2.imshow("Flipped Both Image", flipped_image_both)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Canny Edges", canny_edges)

# Wait until a key is pressed and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
