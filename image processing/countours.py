
import cv2 



def countours(gray,img):
    ret,tresh=cv2.threshold(gray,192,210,cv2.THRESH_BINARY)
    countours,hearchy=cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    print(len(countours))
    cv2.drawContours(img,countours,-1,(0,0,255),1)
    
    

img=cv2.imread('image path')  
img=cv2.resize(img,(526,392))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
countours(gray,img)

cv2.imshow('image',img)
cv2.waitKey(0)