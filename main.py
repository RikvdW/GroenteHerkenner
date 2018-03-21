from img_class import image
from Teach_class import Teach
import findObject as FO
import cv2
import glob

tch=Teach()

for imgR in glob.glob("fotos/test imges/*.jpg"):
    print(imgR)
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
    tch.Predict(img.data)
    #img.dataPrint()
    img.showImg()
