## Resizing and cropping
import cv2
import numpy as np
img = cv2.imread("S://study/course/computervision.zone/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("imgResize",imgResize)
cv2.imshow("imgCropped",imgCropped)

cv2.waitKey(0) 