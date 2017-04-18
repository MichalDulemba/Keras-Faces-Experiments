import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
def readimagesfromfolder(path, color, show):
	for filename in os.listdir(path):
		fullfilename =  path + filename
		singleimage = cv2.imread(fullfilename,color)
		if show==1:
			cv2.imshow("okno", singleimage)
			cv2.waitKey()
		package = np.append(np.array(singleimage))
	cv2.destroyAllWindows()
	return imagepackage

folderpath = '/home/michal/Dokumenty/faces/test'
paczka=readimagesfromfolder(folderpath,1,1)
print np.shape(paczka)

