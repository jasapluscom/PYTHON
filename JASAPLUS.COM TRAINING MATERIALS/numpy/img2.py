#!/usr/bin/env python3
'''
img2.py 
demo for python course
at www.jasaplus.com
'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('img1.png')
imgplot = plt.imshow(img)
plt.show()

print(img)

formatted = (img * 255 / np.max(img)).astype('uint8')
img2 = Image.fromarray(formatted)
img2.show()

print(formatted)