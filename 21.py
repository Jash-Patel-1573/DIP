import cv2
import numpy as np

# Load the binary image
image = cv2.imread('binary_image.png', cv2.IMREAD_GRAYSCALE)

# Define a kernel for the morphological operations
kernel = np.ones((5, 5), np.uint8)

# Dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Opening (Erosion followed by Dilation)
opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing (Dilation followed by Erosion)
closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Opening Image', opening_image)
cv2.imshow('Closing Image', closing_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
