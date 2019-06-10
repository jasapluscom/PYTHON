#!/usr/bin/env python3
'''
img5.py 
demo for python course
at www.jasaplus.com
'''
import numpy as np
from PIL import Image
img = Image.open('10px.png')
arr = np.array(img)
img_no_alpha = arr[:,:,:3]

for i in range(0 , 10) : 
    img_no_alpha[0, i] =  [0,0,0]
modif = Image.fromarray(img_no_alpha)
modif.save("modif.png")
img_no_alpha[0, 0:10] =  [255,255,255]
modif2 = Image.fromarray(img_no_alpha)
modif2.save("modif2.png")
