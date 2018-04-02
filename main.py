from img_class import image
from Teach_class import Teach
import findObject as FO
import cv2
import glob

tch=Teach()

for imgR in glob.glob("fotos/test imges/*.jpg"):
    print(imgR)
    img = image(imgR) 
    img.resize()            #afbeelding verkleinen
    img.BGR2RGB()           #Kleuren omzetten van BGR naar RGB
    img.gauss()             #GaussionBlur op afbeelding toepassen
    img.RGB2HSV()           #Kleur omzetten van RGB naar HSV
    img.filter()            #
    img.findCont()          #contours vinden 
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
