from img_class import image

img = image("balls.png")
img.dataPrint()
img.grayScale()
img.adaptiveThreshold()

img.dilate(1)
img.median(3)
img.erode(3)
img.median(9)
img.fill()
img.showImg()
print("help")
print("help2")
