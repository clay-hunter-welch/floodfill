#!/usr/bin/python
from __future__ import print_function
import argparse
import struct
import scipy
import scipy.misc
import scipy.cluster
import numpy
from PIL import Image 

parser = argparse.ArgumentParser(
	prog='floodfill.py',
	description='Reads an image and performs a floodfill color substitution on the dominant color.',
	epilog='Drink your Ovaltine.')

parser.add_argument('image_file')	#positional argument
#parser.add_argument('-i', '--invert', action='store_true')
parser.add_argument('-t', '--threshhold', type = int)
args = parser.parse_args()
t = args.threshhold

print('reading image')
image = Image.open(args.image_file)
pixdata = image.load()

'''
scale image down to one pixel without resample; the idea is that this remaining pixel is the most represented
color in the image file.
'''
image_sm = image.resize((1, 1), resample=0)
dominant_color = image.getpixel((0,0))
dom_r = dominant_color[0]
dom_g = dominant_color[1]
dom_b = dominant_color[2]
print('dominant color: ',dominant_color)

'''
for each pixel in the image, test if the pixel r,g,b values fall within the threshhold distance of the dominant color.
if so, replace with red.
'''
for y in range(image.size[1]):
	for x in range(image.size[0]):
		pix_r = pixdata[x,y][0]
		pix_g = pixdata[x,y][1]
		pix_b = pixdata[x,y][2]
		
		if pix_r <= (dom_r + t) and pix_g <= (dom_g + t) and pix_b <= (dom_b + t) and pix_r >= (dom_r - t) and pix_g >= (dom_g - t) and pix_b >= (dom_b - t):
			pixdata[x,y] = (255, 1, 1)

image.show()

image.close()
