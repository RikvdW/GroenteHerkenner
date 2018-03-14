from img_class import image
from Teach_class import Teach

img = image("fotos/auburgine1.jpeg")
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
img.showImg()
