import glob
import cv2
import numpy as np
from img_class import image
from Teach_class import Teach
import pickle

data=[]
labels=[]

for imgR in glob.glob("fotos/prei/*.jpg"):
    img = image(imgR)
    img.resize()
    img.BGR2RGB()
    img.gauss()
    img.RGB2HSV()
    img.filter()
    img.findCont()
    img.subimage()
    img.getHSvalue()
    img.QuantiseHvalue()
    img.getLineHSvalue()
    img.Texture()
    img.HSV2BGR()
    img.makeData()
    data.append(img.data)
    #img.showImg()
    labels.append(1)
for imgR in glob.glob("fotos/aubergine/*.jpg"):
    img = image(imgR)
    img.resize()
    img.BGR2RGB()
    img.gauss()
    img.RGB2HSV()
    img.filter()
    img.findCont()
    img.subimage()
    img.getHSvalue()
    img.QuantiseHvalue()
    img.getLineHSvalue()
    img.Texture()
    img.HSV2BGR()
    img.makeData()
    data.append(img.data)
    #img.showImg()
    labels.append(2)
for imgR in glob.glob("fotos/Radijs/*.jpg"):
    img = image(imgR)
    img.resize()
    img.BGR2RGB()
    img.gauss()
    img.RGB2HSV()
    img.filter()
    img.findCont()
    img.subimage()
    img.getHSvalue()
    img.QuantiseHvalue()
    img.getLineHSvalue()
    img.Texture()
    img.HSV2BGR()
    img.makeData()
    #img.showImg()
    #tch=Teach()
    #tch.Predict(img.data)
    data.append(img.data)
    labels.append(3)
for imgR in glob.glob("fotos/wortel/*.jpg"):
    img=image(imgR)
    img.resize()
    img.BGR2RGB()
    img.gauss()
    img.RGB2HSV()
    img.filter()
    img.findCont()
    img.subimage()
    img.getHSvalue()
    img.QuantiseHvalue()
    img.getLineHSvalue()
    img.Texture()
    img.HSV2BGR()
    img.makeData()
    #img.showImg()
    #tch.Predict(img.data)
    data.append(img.data)
    labels.append(4)
for imgR in glob.glob("fotos/Broccoli/*.jpg"):
    img=image(imgR)
    img.resize()
    img.BGR2RGB()
    img.gauss()
    img.RGB2HSV()
    img.filter()
    img.findCont()
    img.subimage()
    img.getHSvalue()
    img.QuantiseHvalue()
    img.getLineHSvalue()
    img.Texture()
    img.HSV2BGR()
    img.makeData()
    #img.showImg()
    #tch.Predict(img.data)
    data.append(img.data)
    labels.append(5)

#print(data)
#print(labels)
output = open('data.pkl', 'wb')
pickle.dump(data, output)


outputL = open('labels.pkl', 'wb')
pickle.dump(labels, outputL)


#print(labels)
#print(data)
