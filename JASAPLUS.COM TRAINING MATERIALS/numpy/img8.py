#!/usr/bin/env python3
'''
img8.py 
demo for python course
at www.jasaplus.com
'''
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = mpimg.imread('cat.jpg')
gray = rgb2gray(img)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()

formatted = (gray * 255 / np.max(gray)).astype('uint8')
cr = Image.fromarray(formatted)
cr.save("gray.jpg")
