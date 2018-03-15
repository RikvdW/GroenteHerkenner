import numpy as np
import cv2
import math

def helloworld(mask):
      #print ("hello world")
      #cv2.imshow("maksbla", mask)

      ellipse = cv2.fitEllipse(mask)
      img = cv2.ellipse(mask,ellipse,(0,255,0),4)

      """

      im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

      rows,cols = mask.shape[:2]
      [vx,vy,x,y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
      lefty = int((-x* vy / vx) + y)
      righty = int(((cols-x) * vy / vx) + y)
      img = cv2.line(mask,(cols-1,righty),(0,lefty),(0,255,0),2)

      """

      cv2.imshow("lines", img)

      """

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
      skel=cv2.dilate(skel, element)
      skel=cv2.dilate(skel, element)
      skel=cv2.dilate(skel, element)
      skel=cv2.dilate(skel, element)
      #dingen proberen
      gray = np.copy(skel)

      edges = cv2.Canny(gray,50,200, None, 3)

      gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

      kernel = np.ones((15,15),np.uint8)

      skel = cv2.morphologyEx(skel, cv2.MORPH_CLOSE, kernel)

      #cv2.imshow("skelsej3", skel)

      minLineLength = 1000
      maxLineGap = 0
<<<<<<< HEAD

      lines = cv2.HoughLinesP(skel, 1, np.pi/180,100, minLineLength,maxLineGap)

      print(lines[0])
      
=======
      lines = cv2.HoughLinesP(edges, 1, np.pi/180,100, minLineLength,maxLineGap)
      #print(lines[0])
>>>>>>> 860922f6e610208f56533e63bccf6f4787c7849c
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

      

      for x1,y1,x2,y2 in lines[0]:
             print("hello")
             cv2.line(edges,(x1,y1),(x2,y2),(255,255,255),10)

      
      for line in lines:
            for x1,y1,x2,y2 in line:
                  print("hello")
                  cv2.line(edges,(x1,y1),(x2,y2),(255,255,255),10)
      """

<<<<<<< HEAD
      
      
=======

      #for x1,y1,x2,y2 in lines[0]:
       #       print("hello")
        #      cv2.line(edges,(x1,y1),(x2,y2),(255,255,255),200)
>>>>>>> 860922f6e610208f56533e63bccf6f4787c7849c

      cv2.imshow("lines", edges)
