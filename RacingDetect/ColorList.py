import numpy as np
import collections

def getColorList():
    dict = collections.defaultdict(list)

    #blue
    lower_blue = np.array([100, 100, 46])
    upper_blue = np.array([124, 255, 255])
    bgr = (255, 0, 0)
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    color_list.append(bgr)
    dict['blue'] = color_list

    #black
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 160])
    bgr = (0, 0, 0)
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    color_list.append(bgr)
    dict['black']=color_list

    #green
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([90, 255, 255])
    bgr = (0, 255, 0)
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    color_list.append(bgr)
    dict['green'] = color_list

    return dict

if __name__ == '__main__':
    color_dict = getColorList()
    print(color_dict)

    num = len(color_dict)
    print('num=',num)

    for d in color_dict:
        print('key=',d)
        print('value=',color_dict[d][1])
        print('BGR=',color_dict[d][2])
