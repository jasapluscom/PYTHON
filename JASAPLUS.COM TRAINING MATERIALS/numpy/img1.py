#!/usr/bin/env python3
'''
img1.py 
demo for python course
at www.jasaplus.com
'''
import numpy as np
from PIL import Image
img = Image.open('img1.png')
array = np.array(img)
print("array shape : " , array.shape)
print("array dim : ", array.ndim)
img.show()
print("\n\n")
print(array)