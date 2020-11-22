import os
import cv2
from sys import flags
import threading
import tkinter as tk
import screeninfo
import time

from PIL import ImageTk, Image
 
#分辨率
resolution = (1920, 1080)
# 路径
original_photo_path = './original_photos'
frame_photo_path = './frame_photos'
alpha_photo_path = './alpha_photos'
final_photo_path = './alpha_photos'
# 播放间隔
interval = 1/60

def add_photo_frame(original_photo_path, frame_photo_path):
    flag = 0
    img_names = os.listdir(original_photo_path)
    frame = cv2.imread("photo_frame.png")

    # 为相片加上相框
    for img_name in img_names:
        img = cv2.imread(original_photo_path + '/' + img_name)
        img =  cv2.resize(img, (1025, 575))
        frame = cv2.resize(frame, (1280,720))
        frame[75:650,125:1150,:] = img
        img_name = frame_photo_path + "/photo" + str(flag).zfill(3) + ".jpg"
        cv2.imwrite(img_name, frame)
        flag += 1

def add_alpha_parameter(frame_photo_path, alpha_photo_path):
    flag = 0
    img_names = os.listdir(frame_photo_path)

    for i in range(len(img_names)):
        before_img = cv2.imread(frame_photo_path + '/' + img_names[i])
        after_img = cv2.imread(frame_photo_path + '/' + img_names[(i + 1) % len(img_names)])
        before_img = cv2.resize(before_img, resolution)
        after_img = cv2.resize(after_img, resolution)
        for j in range(120):
            overlapped_photo = cv2.addWeighted(before_img, 1 - 1/120*j, after_img, 1/120*j, 0)
            img_name = alpha_photo_path + "/photo" + str(flag).zfill(5) + ".jpg"
            cv2.imwrite(img_name, overlapped_photo)
            flag = flag + 1

if __name__ == "__main__":
    add_photo_frame(original_photo_path, frame_photo_path)
    add_alpha_parameter(frame_photo_path, alpha_photo_path)
    img_all = os.listdir(final_photo_path)
    screen = screeninfo.get_monitors()[0]
    window_name = "电子相框"
    cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name,screen.x-1,screen.y-1)
    cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    i = 0
    key = 0
    while (True):
        print(key)
        if (key == ord('q')):
                break
        while(True):
            print(key)
            img = cv2.imread(final_photo_path + '/' + img_all[i])
            cv2.imshow(window_name, img)
            key = cv2.waitKey(1)
            if (i % 120 == 0):
                time.sleep(3)
            if (key == ord('q')):
                break
            else:
                i = (i+1) % len(img_all)
                time.sleep(interval)
        
    cv2.destroyAllWindows()
