#!/usr/bin/env python3
'''
img9.py 
demo for python course
at www.jasaplus.com
'''
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('cat.jpg')
img2 = np.rot90(img)
img_final = Image.fromarray(img2)

img3 = np.rot90(img_final)
img_final = Image.fromarray(img3)
img_final.show()