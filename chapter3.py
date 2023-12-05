from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

def negative_transform(imgpath):
    img = Image.open(imgpath)
    img_array = np.array(img)

    negative_img_array = 255 - img_array
    negative_image = Image.fromarray(negative_img_array)

    return negative_image

def thresholding_image(imgpath):
    gray_image = cv2.cvtColor(imgpath, cv2.COLOR_BGR2GRAY)
    _, threshold_image =  cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    
    pil_image = Image.fromarray(threshold_image)
    return pil_image

def logarit_transform(img_raw):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    c = 255/(np.log(1 + np.max(img))) 
    log_transformed = c * np.log(1 + img) 
  
    # Specify the data type. 
    log_transformed = np.array(log_transformed, dtype = np.uint8)
    pil_image = Image.fromarray(log_transformed)
    return pil_image

def power_law_transform(img_raw, gamma):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') 
    
    pil_image = Image.fromarray(gamma_corrected)
    return pil_image

def histogram_equalizing(img_raw):
    img_to_yuv = cv2.cvtColor(img_raw,cv2.COLOR_BGR2YUV)
    img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
    hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

    pil_image = Image.fromarray(hist_equalization_result)
    return pil_image

def average_filter(img_raw):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    m, n = img.shape 

    mask = np.ones([3, 3], dtype = int) 
    mask = mask / 9
    img_new = np.zeros([m, n])

    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
            
            img_new[i, j]= temp 

    img_new = img_new.astype(np.uint8) 

    pil_image = Image.fromarray(img_new)
    return pil_image

def weighted_averaging(img_raw):
    kernel = (
        np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16
    )  
    processedImage = cv2.filter2D(img_raw, -1, kernel)
    pil_image = Image.fromarray(processedImage)
    return pil_image

def median_filter(img_raw):
    img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    m, n = img.shape 

    img_new1 = np.zeros([m, n])
    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = [img[i-1, j-1], 
                img[i-1, j], 
                img[i-1, j + 1], 
                img[i, j-1], 
                img[i, j], 
                img[i, j + 1], 
                img[i + 1, j-1], 
                img[i + 1, j], 
                img[i + 1, j + 1]] 
            
            temp = sorted(temp) 
            img_new1[i, j]= temp[4] 
    
    img_new1 = img_new1.astype(np.uint8) 
    pil_image = Image.fromarray(img_new1)
    return pil_image

imgpath = 'D:/ImageProcessAlgorithm/image/anh-3d-thien-nhien.jpeg'
imgpath2 = 'D:/ImageProcessAlgorithm/image/moon.jpg'
imgpath3 = 'D:/ImageProcessAlgorithm/image/cpu.jpg'
imgpath4 = 'D:/ImageProcessAlgorithm/image/tiger.jpg'

# negative_transform(imgpath4)
# thresholding_image(imgpath2)
# logarit_transform(imgpath2)
# power_law_transform(imgpath2, 0.5)
# histogram_equalizing(imgpath2)
# average_filter(imgpath3)
# median_filter(imgpath3)