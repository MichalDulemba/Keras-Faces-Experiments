singleimagepath = mainfolder + "/test/"
imagepackage = []
imagelist = []
wrong = 0 
total = 0
categories = ["jackie", "obama", "empty", "rachel"]
filelist = sorted(os.listdir(singleimagepath))

for filename, realcategory in izip(filelist,y_test):
    #print filename
    fullfilename =  singleimagepath + filename
    singleimage = imageio.imread(fullfilename)
    singleimage = cv2.resize(singleimage,(96,96), interpolation=cv2.INTER_AREA)        
    gray = rgb2gray(singleimage)

    imagepackage_list = gray.reshape((1, 1, 96, 96))
    #print imagepackage_list.shape
    
    result = model.predict(imagepackage_list, batch_size=1, verbose=0)
    
    for x,y in izip(realcategory, result):
        if not np.array_equal(realcategory, result[0]):
            print "wrong"
            print "Real category", realcategory
            print "Prediction", result[0]
            
            plt.imshow(gray, cmap = plt.get_cmap('gray'))
            plt.show()
            wrong += 1
    total += 1
    
    imagepackage_list = []
    imagepackage = []  

print "wrong - ",wrong, "of total" ,total
