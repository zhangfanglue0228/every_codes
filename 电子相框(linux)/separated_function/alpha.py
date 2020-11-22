import cv2
import os

#分辨率
resolution = (1920, 1080)
flag = 0
old_photo_path = './frame_photos'
new_photo_path = './alpha_photos'
img_names = os.listdir(old_photo_path)

for i in range(len(img_names)):
    before_img = cv2.imread(old_photo_path + '/' + img_names[i])
    after_img = cv2.imread(old_photo_path + '/' + img_names[(i + 1) % len(img_names)])
    before_img = cv2.resize(before_img, resolution)
    after_img = cv2.resize(after_img, resolution)
    for j in range(120):
        overlapped_photo = cv2.addWeighted(before_img, 1 - 1/120*j, after_img, 1/120*j, 0)
        img_name = new_photo_path + "/photo" + str(flag).zfill(5) + ".jpg"
        cv2.imwrite(img_name, overlapped_photo)
        flag = flag + 1

