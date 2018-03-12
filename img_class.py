import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



class image:
    Operations=[]
    ones_kernel = np.ones((4,4),np.uint8)
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
        print ("TextBusy" + str(self.TextBusy))
        if (len(self.Operations)>0):
            print ("Operations:")
            for i in range(0,len(self.Operations)):
                print (str(i+1) + ":" +self.Operations[i])
        else:
            print ("No operations")
        plt.figure()
        plt.title("Horizontal image line")
        plt.xlabel("X-Position")
        plt.ylabel("Intensity")
        plt.plot(self.Hlinearray,'r')
        plt.plot(self.Slinearray,'b')
        plt.plot(self.Harray,'g')

        plt.show()

    def showOrgImg(self):
        cv2.imshow("orignial image", self.org_img)
        cv2.waitKey(0)

    def showImg(self):
        cv2.imshow("Image", self.img)
        cv2.waitKey(0)

    def resize(self):
        max_dim=max(self.img.shape)
        scale=700/max_dim
        self.img= cv2.resize(self.img, None, fx=scale, fy=scale)

    def grayScale(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.Operations.append("grayScale")

    def BGR2RGB(self):
        self.img=cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.Operations.append("To RGB")

    def RGB2HSV(self):
        self.img=cv2.cvtColor(self.img, cv2.COLOR_RGB2HSV)
        self.Operations.append("To HSV")

    def HSV2BGR(self):
        self.img=cv2.cvtColor(self.img, cv2.COLOR_HSV2BGR)
        self.Operations.append("To BGR")

    def adaptiveThreshold(self):
        self.img = cv2.adaptiveThreshold(self.img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
        self.Operations.append("adaptiveThreshold")

    def GammaCorection(self, gamma):
          invGamma = 1.0 / gamma
          table = np.array([((i / 255.0) ** invGamma) * 255
             for i in np.arange(0, 256)]).astype("uint8")
          self.img= cv2.LUT(self.img, table)

    def gauss(self):
        self.img=cv2.GaussianBlur(self.img,(7,7),1)
        self.Operations.append("Median")

    def erode(self, n):
        self.img=cv2.erode(self.img,self.ones_kernel,iterations = n)
        self.Operations.append("Erode")

    def dilate(self, n):
        self.img=cv2.dilate(self.img,self.ones_kernel,iterations = n)
        self.Operations.append("Dilate")

    def filter(self):
        min_red = np.array([10,40,50])
        max_red = np.array([256,256,256])
        mask1 = cv2.inRange(self.img, min_red, max_red)
        min_red2 = np.array([0,30,0])
        max_red2 = np.array([256,256,256])
        mask2 = cv2.inRange(self.img, min_red2, max_red2)
        mask = (mask1+mask2)

        mask=cv2.erode(mask,self.ones_kernel,iterations = 3)
        mask=cv2.dilate(mask,self.ones_kernel,iterations = 3)

        self.mask=mask
        self.img = mask
        #self.img = cv2.bitwise_and(self.img,self.img, mask= mask)
    def getHSvalue(self):
        img_h=self.img[:,:,0]
        img_s=self.img[:,:,1]
        self.hist_s = cv2.calcHist([self.img[:,:,0]],[0],None,[256],[1,256])
        self.hist_h = cv2.calcHist([self.img[:,:,1]],[0],None,[256],[1,256])

    def QuantiseHvalue(self):
        self.Harray=[0,0,0,0,0,0]
        for i in range(0,5):
            for j in range(1,int(len(self.hist_h)/5)):
                self.Harray[i]+=self.hist_h[j*(1+i)]

    def getLineHSvalue(self, n):
        img_h=self.img[n,:,0]
        img_s=self.img[n,:,1]
        self.Hlinearray=[0,0,0,0,0,0]
        self.Slinearray=[0,0,0,0,0,0]
        for i in range(0,5):
            for j in range(1,int(len(img_h)/5)):
                #print (self.hist_h[j])
                self.Hlinearray[i]+=img_h[j*(1+i)]
                self.Slinearray[i]+=img_s[j*(1+i)]
        if(self.Hlinearray[len(self.Hlinearray)-1]>self.Hlinearray[0]):
            self.Hlinearray=self.Hlinearray[::-1]
        if(self.Slinearray[len(self.Slinearray)-1]>self.Slinearray[0]):
            self.Slinearray=self.Slinearray[::-1]

    def Texture(self):
        cany= cv2.Canny(self.img[:,:,1],1,100)
        canyHist = cv2.calcHist([cany],[0],None,[256],[1,256])
        self.TextBusy = 0
        for i in range(1,len(canyHist)):
            self.TextBusy+=canyHist[i]
