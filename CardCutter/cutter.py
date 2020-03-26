import imageio
import numpy as np
import cv2 as cv

from os import listdir
from os.path import isfile, join

def procc_image(img_file,cut=[207,580,250,1180],name='test.png'):
	img_data = cv.imread(img_file)
	img_data = img_data[cut[0]:cut[1], cut[2]:cut[3], :]
	cv.imwrite(join('./Cards/Cut',name), img_data) 
	return img_data

if __name__ == '__main__':
	mypath = './Cards'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	for i,image in enumerate(onlyfiles):
		if image=='.DS_Store':
			continue
		procc_image(join('./Cards',image),name=str(i)+'.png')