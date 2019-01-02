import cv2
import numpy as np
import time

cam = cv2.VideoCapture("rtsp://admin:c217camera@10.10.217.139/stream1")
CHECKERBOARD = (8, 5)
i = 1
while(True):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
    if ret == True :
        cv2.imwrite('./image/'+'test_'+str(i)+'.jpeg', frame)
        print('test_'+str(i)+'.jpeg')
        i += 1
    else :
        print(ret)
