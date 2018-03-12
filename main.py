from img_class import image

img = image("fotos/wortel1.jpeg")

img.GammaCorection(1)
img.resize()
img.BGR2RGB()
img.gauss()
img.RGB2HSV()
img.filter()
#img.getHSvalue()
#img.QuantiseHvalue()
#img.getLineHSvalue(150)
#img.Texture()
#img.HSV2BGR()
#img.dataPrint()
img.showImg()
#img.showOrgImg()
