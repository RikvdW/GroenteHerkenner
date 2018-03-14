from img_class import image
from Teach_class import Teach
import findObject as FO
import cv2





img = image("fotos/prei.jpeg")
img.resize()
img.BGR2RGB()
img.gauss()
img.RGB2HSV()
img.filter()
img.getHSvalue()
img.QuantiseHvalue()
img.getLineHSvalue(150)
img.Texture()
img.HSV2BGR()
img.makeData()
tch=Teach()
tch.Predict(img.data)
img.getHSvalue()
img.QuantiseHvalue()
#img.HSV2BGR()
#img.dataPrint()
#FO.helloworld(img.mask)
img.findCont()
img.subimage()
img.showImg()
