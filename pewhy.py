import cv2
import numpy as np
import time

vid = cv2.VideoCapture("videa.mp4")
count = 0
background = 0
for i in range(60):
    return_val, background = vid.read()
    if return_val == False:
        continue
    background = np.flip(background,axis = 1) #axis 1 = flipping the image horizontally because webcam style videos are often displayed as a mirror image

while(vid.isOpened()):
    return_val, img = vid.read()
    if not return_val:
        break
    count = count + 1
    img = np.flip(img,axis = 1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_red = np.array([100,40,40]) #100 = hue 40 = saturation 40 = value
    upper_red = np.array([100,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    lower_red2 = np.array([170,40,40]) #100 = hue 40 = saturation 40 = value
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red2,upper_red2) 
    mask = mask1 + mask2
    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        np.ones((3,3),np.uint8,
                iterations = 2)
    )
    mask = cv2.dilate(mask, np.ones((3,3)),np.uint8,
                    iterations = 1)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background,background,mask=mask)
    res2 = cv2.bitwise_and(img,img,mask = mask2)
    finaloutput = cv2.addWeighted(
        res1,1,
        res2,1,
        0
    )
    cv2.imshow("invisible guy",finaloutput)
    k = cv2.waitKey(10)
    if k == 27:
        break
    

