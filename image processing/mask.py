
import numpy as np
import cv2
from  matplotlib import pyplot as plt


# Load an color image in grayscale
img=cv2.imread('5.png')
img = cv2.resize(img, (512,512))/255


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist_image=cv2.equalizeHist(gray)


img_gaussian = cv2.GaussianBlur(gray,(3,3),0)


cv2.imshow("Gray", img)

cv2.waitKey(0)


#hist_equa_image
hist_image=cv2.equalizeHist(img)
hist_image = cv2.medianBlur(hist_image,3)
hist_image = cv2.medianBlur(hist_image,3)

cv2.imshow("hist_image", hist_image)
#histograme

plt.hist(img.ravel(),255,[0,255])
plt.show()


#threshold
_, th=cv2.threshold(hist_image,176,150,cv2.THRESH_BINARY)


#canny

img_canny = cv2.Canny(th,148,255)
cv2.imshow("Canny", img_canny)



img_canny = cv2.Canny(hist_image,154,250)
cv2.imshow("Canny_hist", img_canny)


#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely
cv2.imshow("sobel_image", img_sobel)


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img_prewitt=img_prewittx+img_prewitty
#cv2.imshow("prew", img_prewitt)


#hsv with inrange
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (77,70,70), (250, 250, 250))
dst1 = cv2.bitwise_and(img, img, mask=mask)


GlobuleTaches = cv2.inRange(hsv,(53, 0, 0), (167, 255, 255))
Taches = cv2.inRange(hsv,(0, 91, 104), (179, 255, 255))
cv2.imshow("gl", GlobuleTaches)
cv2.imshow("t", Taches)

cv2.waitKey(0)
cv2.destroyAllWindows()