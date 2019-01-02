import cv2
import numpy as np
import json
from ColorList import getColorList
import socket
import time

cam = cv2.VideoCapture("http://admin:c217camera@10.10.217.187/mjpg/1/video.mjpg")
#map1 = np.load('map1.npy')
#map2 = np.load('map2.npy')
lower_white = np.array([0, 0, 200], dtype=np.uint8)
upper_white = np.array([180, 30, 255], dtype=np.uint8)
lower_red = np.array([156, 43, 46], dtype=np.uint8)
upper_red = np.array([180, 255, 255], dtype=np.uint8)
kernel_map = np.ones((25, 25),np.uint8)
kernel_color = np.ones((3, 3),np.uint8)
color_dict = getColorList()
ip = '10.10.217.255'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)



def CoordinateCaculate(frame=None, lower=None, upper=None, kernel=None, color=None):
    global points
    #if color == 'white' or color == 'red':
    #    calibration = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    #else:
    #    calibration = frame
    calibration = frame
    hsv = cv2.cvtColor(calibration, cv2.COLOR_BGR2HSV)
    foo = cv2.inRange(hsv, lower, upper)
    res, threshold = cv2.threshold(foo, 127, 255, cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    image ,contours,hierarchy = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        cnt = sorted(contours, key = cv2.contourArea, reverse = True)[0]
        rect = cv2.minAreaRect(cnt)
        points = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        '''if color == 'white' or color == 'red':
            for i,foo in enumerate(points):
                if i == 0:
                    points[i] = [foo[0]+10, foo[1]-10]
                if i == 1:
                    points[i] = [foo[0]+12, foo[1]+12]
                if i == 2:
                    points[i] = [foo[0]-10, foo[1]]
                if i == 3:
                    points[i] = [foo[0], foo[1]]'''
    return points, color


while(1):
    try:
        _, frame = cam.read()
        #output = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
        output = frame
        frame1 = frame[0:, 0:500]
        cv2.imshow('test', frame)

        coordinate, color = CoordinateCaculate(frame1, lower_white, upper_white, kernel_map, 'white')
        #inside_points, bar = CoordinateCaculate(frame1, lower_red, upper_red, kernel_color, 'red')
        #cv2.drawContours(output, [inside_points], -1, [0,0,255], 3)
        outside_data = coordinate.tolist()
        #inside_data = inside_points.tolist()
        map_data = {'outside': outside_data}
        '''foo1 = json.dumps(map_data)
        map_json = foo1.encode()
        sock.sendto(map_json, (ip, 5005))
        for i,point in enumerate(coordinate):
            coordinate[i] = [point[0]+500, point[1]]'''
        cv2.drawContours(output, [coordinate], -1, [0,0,255], 3)
        cut_x = [int(coordinate[0][0]), int(coordinate[-1][0])]
        cut_y = [int(coordinate[2][1]), int(coordinate[3][1])]
        frame1 = frame[cut_y[0]:cut_y[1],cut_x[0]:cut_x[1]]
        for d in color_dict:
            foo = str(d)
            Color_points, foo =CoordinateCaculate(frame1, color_dict[d][0], color_dict[d][1], kernel_color, foo)
            for i, points in enumerate(Color_points):
                #Color_points[i] = [points[0]+cut_y[0], points[1]+cut_y[1]]
                print(Color_points[i])
            cv2.drawContours(output, [Color_points], -1, color_dict[d][2], 2)
            '''Color_points = Color_points.tolist()
            data = {foo : Color_points, 'time': stime}
            json_data = json.dumps(data)
            json_output = json_data.encode()
            if foo == 'green':
                sock.sendto(json_output, (ip, 5487))
            if foo == 'black':
                sock.sendto(json_output, (ip, 8787))
            if foo == 'blue':
                sock.sendto(json_output, (ip, 1234))'''

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    except cv2.error:
        print('cvtColorError')
        continue

cv2.destroyAllWindows()
