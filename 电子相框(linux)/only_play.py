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
final_photo_path = './alpha_photos'
# 播放间隔
interval = 1/60

# 调用Linux csi相机
# def gstreamer_pipeline(
#     capture_width=1280,
#     capture_height=720,
#     display_width=1280,
#     display_height=720,
#     framerate=60,
#     flip_method=0,
# ):
#     return (
#     "nvarguscamerasrc ! "
#     "video/x-raw(memory:NVMM), "
#     "width=(int)%d, height=(int)%d, "
#     "format=(string)NV12, framerate=(fraction)%d/1 ! "
#     "nvvidconv flip-method=%d ! "
#     "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
#     "videoconvert ! "
#     "video/x-raw, format=(string)BGR ! appsink"
#             % (
#                 capture_width,
#                 capture_height,
#                 framerate,
#                 flip_method,
#                 display_width,
#                 display_height,
#             )
#         )

# 调用windows电脑相机
# def show_camera():
#     cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
#     while cap.isOpened():
#         flag, img = cap.read()
#         cv2.imshow("CSI Camera", img)
#         kk = cv2.waitKey(1)
#         # do other things
#         if kk == ord('q'):  # 按下 q 键，退出
#             break
#     cap.release()

def show_camera():
    global flag
    cap=cv2.VideoCapture(0)
    while True:
        cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        #从摄像头读取图片
        sucess,img=cap.read()
        #重设大小
        img = cv2.resize(img, (1728, 1296))
        cv2.imshow("CSI Camera", img)
        #保持画面的持续。
        k=cv2.waitKey(1)
        if (k == ord('q')):
            #通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif (k == ord("s")):
            #通过s键保存图片，并退出。
            cv2.imwrite("saved_photos/photo" + str(flag).zfill(3) + ".jpg", img)
            flag = flag + 1
    #关闭摄像头
    cap.release()
    cv2.destroyAllWindows()

# 读取照片名字
img_all = os.listdir(final_photo_path)
img_all.sort()

screen = screeninfo.get_monitors()[0]
window_name = "电子相框"
i = 0
key = 0
flag = 0

while(True):
    cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name,screen.x-1,screen.y-1)
    cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    if (key == ord('q')):
        break
    while(True):
        img = cv2.imread(final_photo_path + '/' + img_all[i])
        cv2.imshow(window_name, img)
        key = cv2.waitKey(1)
        # if (i % 120 == 0):
        #     time.sleep(3)
        if (key == ord('q')):
            break
        elif(key == ord('c')):
            show_camera()
            break
        else:
            i = (i+1) % len(img_all)
            time.sleep(interval)
    
cv2.destroyAllWindows()
