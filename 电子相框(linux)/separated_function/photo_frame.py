import cv2
import numpy as np
from  matplotlib  import pyplot as plt
import os

old_photo_path = './old_photos'
new_photo_path = './frame_photos'
flag = 0

img_names = os.listdir(old_photo_path)
frame = cv2.imread("photo_frame.png")


for img_name in img_names:
    img = cv2.imread(old_photo_path + '/' + img_name)
    img =  cv2.resize(img, (1025, 575))
    frame = cv2.resize(frame, (1280,720))
    frame[75:650,125:1150,:] = img
    img_name = new_photo_path + "/photo" + str(flag).zfill(3) + ".jpg"
    cv2.imwrite(img_name, frame)
    flag += 1

