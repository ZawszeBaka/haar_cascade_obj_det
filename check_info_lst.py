import os
import numpy as np
import cv2

def check_info_lst(num_check=10):
    with open('info.lst', 'r') as f :
        rows = f.read().split('\n')

    i = 0
    for row in rows:
        i += 1
        file_name = row.split()[0]
        img = cv2.imread('info/'+file_name)
        x = int(row.split()[2])
        y = int(row.split()[3])
        w = int(row.split()[4])
        h = int(row.split()[5])
        img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        print('[INFO] img','info/'+file_name, ' (x,y,w,h) = ', x,y,w,h)
        cv2.imshow('Checking info_lst', img)
        cv2.waitKey()
        if i==num_check:
            break


    cv2.destroyAllWindows()



if __name__ == '__main__':
    check_info_lst(num_check=10)
