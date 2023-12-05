from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

def rlc_coding(image):
    pixels = list(image.getdata())
    width, height = image.size
    encoded_data = []

    for y in range(height):
        current_run = 1
        current_pixel = pixels[y * width]

        for x in range(1, width):
            pixel = pixels[y * width + x]
            if pixel == current_pixel:
                current_run += 1
            else:
                encoded_data.append((current_pixel, current_run))
                current_pixel = pixel
                current_run = 1

        encoded_data.append((current_pixel, current_run))

    compressed_image = Image.new("L", (width, height))
    flat_encoded_data = [item for sublist in encoded_data for item in sublist]
    compressed_image.putdata(flat_encoded_data)
    return compressed_image

def lzw_compress(image):
    pixels = list(image.getdata())
    dictionary = {i: chr(i) for i in range(256)}
    compressed_data = []
    current_code = 256
    sequence = pixels[0]

    for pixel in pixels[1:]:
        combined_sequence = sequence + pixel
        if combined_sequence in dictionary:
            sequence = combined_sequence
        else:
            compressed_data.append(dictionary[sequence])
            dictionary[combined_sequence] = current_code
            current_code += 1
            sequence = pixel

    compressed_data.append(dictionary[sequence])

    compressed_image = Image.new("L", image.size)
    flat_compressed_data = []
    for code in compressed_data:
        flat_compressed_data.extend([ord(char) for char in code])

    # Đặt giá trị pixel của ảnh đã nén
    compressed_image.putdata(flat_compressed_data)
    return compressed_image