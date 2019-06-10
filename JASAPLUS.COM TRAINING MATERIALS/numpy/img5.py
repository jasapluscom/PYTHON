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
'''
cropped = img[y1:y2, x1:x2]
The (x1, y1) would be the top left corner and the (x2, y2) the bottom right.
'''
cropimg = img_no_alpha[1:8, 1:8]
cr = Image.fromarray(cropimg)
cr.save("cropped.png")


