from img_class import image

img = image("balls.png")
img.dataPrint()
img.grayScale()
img.adaptiveThreshold()
img.median(5)
img.erode(2)
img.showImg()

