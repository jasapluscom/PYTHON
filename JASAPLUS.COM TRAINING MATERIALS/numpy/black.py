#!/usr/bin/env python3
'''
black.py 
demo for python course
at www.jasaplus.com
'''
import numpy as np
from PIL import Image


img = Image.open('10px.png')
arr = np.array(img)
img_no_alpha = arr[:,:,:3]

img_no_alpha[:, :] =  [0,0,0]
black = Image.fromarray(img_no_alpha)
black.save("black.png")
