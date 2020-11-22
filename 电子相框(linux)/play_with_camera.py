import cv2
from  matplotlib  import pyplot as plt
import time
import screeninfo

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
    "nvarguscamerasrc ! "
    "video/x-raw(memory:NVMM), "
    "width=(int)%d, height=(int)%d, "
    "format=(string)NV12, framerate=(fraction)%d/1 ! "
    "nvvidconv flip-method=%d ! "
    "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! appsink"
            % (
                capture_width,
                capture_height,
                framerate,
                flip_method,
                display_width,
                display_height,
            )
        )

def show_camera():
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    while cap.isOpened():
        flag, img = cap.read()
        cv2.imshow("CSI Camera", img)
        kk = cv2.waitKey(1)
        # do other things
        if kk == ord('q'):  # 按下 q 键，退出
            break
    cap.release()

if __name__ == "__main__":
    window_name = "电子相框"
    cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
    img_all = []
    screen = screeninfo.get_monitors()[0]
    for i in range(1,21):
        img = cv2.imread("D:/desktop/test/photo"+ str(i)+".jpg")
        img_all.append(img)
    
    cv2.moveWindow(window_name,screen.x-1,screen.y-1)
    cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    i = 0
    key = -1
    while (True):
        if (key == ord('q')):
            break
        while (True):
            cv2.imshow(window_name,img_all[i])
            key = cv2.waitKey(1)
            if(key == ord('q')):
                break
            elif(key == ord('c')):
                show_camera()
                break
            else:
                i = (i+1) % 20
                time.sleep(1)
    cv2.destroyAllWindows()
