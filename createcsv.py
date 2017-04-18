import os
import fnmatch
nr = 0
path = "/home/michal/Dokumenty/faces/test_blond/"
listaplikow = sorted(os.listdir(path))
with open("test_blond.csv", "w+") as f: 
	for filename in listaplikow:
		if fnmatch.fnmatch(filename,"*jackie*"):
			#linia = filename + "," + "0\n"
			linia = "0\n"
		elif fnmatch.fnmatch(filename,"*obama*"):
			#linia = filename + "," + "1\n"
	 		linia = "1\n"
		elif fnmatch.fnmatch(filename,"*elisabeth*"):
			#linia = filename + "," + "2\n"
	 		linia = "2\n"
		elif fnmatch.fnmatch(filename,"*rachel*"):
			#linia = filename + "," + "3\n"
	 		linia = "3\n"

		else :
			#linia = filename + "," + "4\n"
			linia = "4\n"

		f.write(linia)
f.close()	



