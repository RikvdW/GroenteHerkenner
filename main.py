from img_class import image
<<<<<<< HEAD
from Teach_class import Teach
=======
import findObject as FO
import cv2



>>>>>>> origin/master

img = image("fotos/auburgine1.jpeg")
img.resize()
img.BGR2RGB()
img.gauss()
img.RGB2HSV()
img.filter()
<<<<<<< HEAD
img.getHSvalue()
img.QuantiseHvalue()
img.getLineHSvalue(150)
img.Texture()
img.HSV2BGR()
img.makeData()
tch=Teach()
tch.Predict(img.data)
=======
#img.getHSvalue()
#img.QuantiseHvalue()
#img.getLineHSvalue(150)
#img.Texture()
img.HSV2BGR()
#img.dataPrint()
FO.helloworld(img.mask)
>>>>>>> origin/master
img.showImg()
