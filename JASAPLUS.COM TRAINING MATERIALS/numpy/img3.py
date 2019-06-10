#!/usr/bin/env python3
'''
img3.py 
demo for python course
at www.jasaplus.com
'''
import skimage 
from skimage import io 
img = io.imread("img1.png") 
print(type(img))
io.imshow(img) 
io.show() 
