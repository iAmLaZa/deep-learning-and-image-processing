import cv2 
from  matplotlib import pyplot as plt
import numpy as np



def simpledetection():
    parms=cv2.SimpleBlobDetector_Params()

    parms.minThreshold=0
    parms.maxThreshold=255

    parms.filterByArea=True
    parms.minArea=20
    parms.maxArea=2000

    parms.filterByCircularity=True
    parms.minCircularity=0.1
    parms.maxCircularity=1


    parms.filterByColor=True
    parms.blobColor=0

    detector=cv2.SimpleBlobDetector_create(parms)

    kp=detector.detect(img)
    print(len(kp))
    imgblob=cv2.drawKeypoints(img,kp,np.array([]),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('123',imgblob)


def nothing(x):
    pass


cv2.namedWindow("tracking")
cv2.createTrackbar("L","tracking",0,255,nothing)
cv2.createTrackbar("H","tracking",0,255,nothing)
cv2.createTrackbar("LV","tracking",0,255,nothing)
cv2.createTrackbar("UH","tracking",255,255,nothing)
cv2.createTrackbar("US","tracking",255,255,nothing)
cv2.createTrackbar("UV","tracking",255,255,nothing)


img=cv2.imread('malaria1.png')  
img=cv2.resize(img,(526,392))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist_image=cv2.equalizeHist(gray)



while(True):
    
    
    l_l=cv2.getTrackbarPos("L","tracking")
    l_h=cv2.getTrackbarPos("H","tracking")
    l_v=cv2.getTrackbarPos("LV","tracking")
    u_h=cv2.getTrackbarPos("UH","tracking")
    u_s=cv2.getTrackbarPos("US","tracking")
    u_v=cv2.getTrackbarPos("UV","tracking")


    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


    lower=np.array([l_h,l_l,l_v ])
    upper=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(img,img,mask=mask)

    _, th=cv2.threshold(hist_image,l_l,l_h,cv2.THRESH_BINARY0)

    cv2.imshow("image",img)
    cv2.imshow("mask",th)
    cv2.imshow("resultat",res)
    key=cv2.waitKey(1)
    if(key== 27):
        break
cv2.destroyAllWindows()

