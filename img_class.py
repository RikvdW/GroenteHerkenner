import cv2
import numpy as np



class image:
    Operations=[]
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
    def intergrate(self):
        self.Operations.append("intergrate")
