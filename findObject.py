import numpy as np
import cv2
import math

def helloworld(mask):
      #print ("hello world")
      #cv2.imshow("maksbla", mask)

      size = np.size(mask)

      element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
      done = False
      skel = np.zeros(mask.shape,np.uint8)
      while( not done):
            eroded = cv2.erode(mask,element)
            temp = cv2.dilate(eroded,element)
            temp = cv2.subtract(mask,temp)
            skel = cv2.bitwise_or(skel,temp)
            mask = eroded.copy()
            zeros = size - cv2.countNonZero(mask)
            if zeros==size:
                  done = True
      #cv2.imshow("skelet", skel)

      #dingen proberen
      gray = np.copy(skel)
      
      edges = cv2.Canny(gray,50,200, None, 3)

      gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

      minLineLength = 0
      maxLineGap = 0
      lines = cv2.HoughLinesP(edges, 1, np.pi/180,100, minLineLength,maxLineGap)
      print(lines[0])
      if lines is not None:
            for i in range(0, len(lines)):
                    rho = lines[i][0][0]
                    theta = lines[i][0][1]
                    a = math.cos(theta)
                    b = math.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                    cv2.line(edges, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)





      #for x1,y1,x2,y2 in lines[0]:
       #       print("hello")
        #      cv2.line(edges,(x1,y1),(x2,y2),(255,255,255),200)
              
      cv2.imshow("lines", edges)
      

