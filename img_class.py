import cv2
import numpy as np



class image:
    Operations=[]
    ones_kernel = np.ones((2,2),np.uint8)
    def __init__(self, link):
        self.link=link
        self.org_img=cv2.imread(link)
        self.img=self.org_img
        self.width=self.img.shape[1]
        self.height=self.img.shape[0]
        self.colours=self.img.shape[2]

    def dataPrint(self):
        print ("Data path: "+ self.link)
        print ("image width: "+ str(self.width) + " height: " + str(self.height))
        print ("Colour channels: " + str(self.colours))
        if (len(self.Operations)>0):
            print ("Operations:")
            for i in range(0,len(self.Operations)):
                print (str(i+1) + ":" +self.Operations[i])
        else:
            print ("No operations")

    def showOrgImg(self):
        cv2.imshow("orignial image", self.org_img)
        cv2.waitKey(0)

    def showImg(self):
        cv2.imshow("Image", self.img)
        cv2.waitKey(0)

    def grayScale(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        self.Operations.append("grayScale")
    def adaptiveThreshold(self):
        self.img = cv2.adaptiveThreshold(self.img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
        self.Operations.append("adaptiveThreshold")
    def median(self, n):
        self.img=cv2.medianBlur(self.img,n)
        self.Operations.append("Median")
    def erode(self, n):
        self.img=cv2.erode(self.img,self.ones_kernel,iterations = n)
        self.Operations.append("Erode")
    def dilate(self, n):
        self.img=cv2.dilate(self.img,self.ones_kernel,iterations = n)
        self.Operations.append("Dilate")
    def fill(self):
        h, w = self.img.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        # Floodfill from point (0, 0)
        cv2.floodFill(self.img, mask, (0,0), 255);

        # Invt floodfilled image
        self.img = cv2.bitwise_not(self.img)
        # Combine the two images to get the for
