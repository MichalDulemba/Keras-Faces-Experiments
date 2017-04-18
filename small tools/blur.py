from sys import argv
import os
import cv2
script, path_old, path_new, kernel_size = argv
nr = 0
#path = "test2/"
#newpath = "test2blurred/"
for filename in os.listdir(path_old):
	fota = cv2.imread(path_old+filename)
	#cv2.imshow("okno",fota)
	print path_old+filename
	fotasmall = cv2.GaussianBlur(fota, (int(kernel_size),int(kernel_size)),0)
	#cv2.imshow("okno",fotasmall)
	cv2.imwrite(path_new+filename, fotasmall)


