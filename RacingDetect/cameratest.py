import cv2
import numpy as np
import time

cam = cv2.VideoCapture("http://admin:c217camera@10.10.217.187/mjpg/1/video.mjpg")

while (True):
    ret, frame = cam.read()
    frame1 = frame[0:, 0:500]
    cv2.imshow("input", frame1)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
