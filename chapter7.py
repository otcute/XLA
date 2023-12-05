from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

# phép co
def erosion_image(img_raw):
    kernel = np.ones((3, 3), np.uint8)
    processedImage = cv2.erode(img_raw, kernel, iterations=1)

    pil_image = Image.fromarray(processedImage)
    return pil_image

# phép giãn
def dilation_image(img_raw):
    processedImage = cv2.convertScaleAbs(img_raw, 1.1, 5)

    pil_image = Image.fromarray(processedImage)
    return pil_image

def closing_image(img_raw):
    kernel = np.ones((3, 3), np.uint8)

    img = cv2.erode(img_raw, kernel, iterations=1)
    processedImage = cv2.convertScaleAbs(img, 1.1, 5)

    pil_image = Image.fromarray(processedImage)
    return pil_image
    
def opening_image(img_raw):
    kernel = np.ones((3, 3), np.uint8)

    img = cv2.dilate(img_raw, kernel, iterations=1)
    processedImage = cv2.erode(img, kernel, iterations=1)

    pil_image = Image.fromarray(processedImage)
    return pil_image

