import numpy as np
import imageio.v2 as imageio
import scipy.ndimage
import cv2

img = "r.png"

def rgb2gray(rgb):
    """Convert RGB image to grayscale"""
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def dodge(front, back):
    """Blend the images to create a sketch effect"""
    result = front * 255.0 / (255 - back + 1e-5)  # Avoid division by zero
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

# Read image
ss = imageio.imread(img)

# Convert to grayscale
gray = rgb2gray(ss).astype('uint8')

# Invert the grayscale image
i = 255 - gray

# Apply Gaussian Blur
blur = scipy.ndimage.gaussian_filter(i, sigma=15)

# Blend images to create the final sketch
r = dodge(blur, gray)

# Save output
cv2.imwrite('final.png', r)
