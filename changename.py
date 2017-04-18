import os
nr = 0
path = "/home/michal/Dokumenty/faces/dopple/ilham/"
for filename in os.listdir(path):
    nowanazwa = "ilhamanas-"+str(nr)+".jpg"
    print (path+filename,path+nowanazwa)
    os.rename(path+filename, path+nowanazwa)
    nr += 1


