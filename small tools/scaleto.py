import os
import cv2
nr = 0
path = "dopple/ilham/"
for filename in os.listdir(path):
	fota = cv2.imread(path+filename)
	fotasmall = cv2.resize(fota, (180,180), interpolation=cv2.INTER_AREA)
	cv2.imwrite(path+filename, fotasmall)


