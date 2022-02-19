import cv2
import numpy as np

from sklearn.decomposition import KernelPCA
from sklearn.preprocessing import KernelCenterer 

##Read Images,Video & Webcam
#for image

img = cv2.imread("computervision.zone/lena.png")

cv2.imshow("Output",img)
cv2.waitKey(0)

#for vedio
"""
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/test_ video.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""

#for web cam
"""
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

