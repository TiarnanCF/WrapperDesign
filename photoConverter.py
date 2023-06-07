import matplotlib.image as mpImg
import matplotlib.pyplot as plt

#Function converting colour image to 2 tone
def biTone(directory,tol,name):
    #read in image
    img = mpImg.imread(directory)
    #define each pixel as black or white based on tolerance
    for i in range(len(img)):
        for j in range(len(img[i])):
            if (img[i][j][0] + img[i][j][1] + img[i][j][2]) < tol:
                img[i][j] = [0,0,0,1]
            else:
                img[i][j] = [1,1,1,1]
    #Get new directory and save image
    location = directory.split("\\")
    location.reverse()
    newdirectory = name + location[0]
    del location[0]
    for layer in location:
        newdirectory = layer + "\\" + newdirectory
    plt.imsave(newdirectory,img)
    
#Function converting colour image to multitone
def multiTone(directory,tols):
    #read in image
    img = mpImg.imread(directory)
    newImg = img.copy()
    #Change colours based on darkness tolerance to colour from selection provided
    for i in range(len(img)):
        for j in range(len(img[i])):
            for tol in tols:
                if (img[i][j][0] + img[i][j][1] + img[i][j][2]) < tol[0]:
                    
                    newImg[i][j] = tol[1].copy()
                    break
    #Get new directory and save image
    location = directory.split("\\")
    location.reverse()
    newdirectory = "new" + location[0]
    del location[0]
    for layer in location:
        newdirectory = layer + "\\" + newdirectory
    plt.imsave(newdirectory,newImg)

#Function merging two photos
def photoMerge(directory1,directory2):
    #Read in images
    img1 = mpImg.imread(directory1)
    img2 = mpImg.imread(directory2)
    
    #Define each pixel as img1 or img2 based on darkness
    for i in range(min(len(img1),len(img2))):
        for j in range(min(len(img1[i]),len(img2[i]))):
            if (img1[i][j][0] + img1[i][j][1] + img1[i][j][2]) < (img2[i][j][0] + img2[i][j][1] + img2[i][j][2]):
                img2[i][j] = img1[i][j].copy()
            else:
                img1[i][j] = img2[i][j].copy()
    
    #Save new image
    location = directory1.split("\\")
    location.reverse()
    newdirectory1 = "modified1.png"
    del location[0]
    for layer in location:
        newdirectory1 = layer + "\\" + newdirectory1
    
    location = directory2.split("\\")
    location.reverse()
    newdirectory2 = "modified2.p/ng"
    del location[0]
    for layer in location:
        newdirectory2 = layer + "\\" + newdirectory2
    
    plt.imsave(newdirectory1,img1)
    plt.imsave(newdirectory2,img2)
