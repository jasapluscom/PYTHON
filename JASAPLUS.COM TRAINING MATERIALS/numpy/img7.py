#!/usr/bin/env python3
'''
img7.py 
demo for python course
at www.jasaplus.com
'''
import numpy as np
from PIL import Image

def _loop_through_all_pixels(img, width, height):
    x = 0
    while x < height:
        y = 0
        while y < width:
            print(img[x, y])
            y += 1
            if y == (width):
                print("_" * 20)
        x += 1
 
img = Image.open('10px.png')
arr = np.array(img)
img_no_alpha = arr[:,:,:3]    
_loop_through_all_pixels(img_no_alpha, 10, 10)