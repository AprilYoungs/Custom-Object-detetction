# -*- coding: utf-8 -*-
# @Time    : 16/12/2018 11:53
# @Author  : April Young
# @Email   : yangchangjun010@hotmail.com
# @File    : clip_video.py
# @Software: PyCharm

import cv2
import numpy as np
import os

path = "/Users/April/Desktop/basketball/basketball.mp4"

root_path = "/".join(path.split("/")[:-1])


cap = cv2.VideoCapture(path)

i = 0
while(cap.isOpened()):

    ret, frame = cap.read()

    i += 1
    if i%200 != 0:
        continue

    if not isinstance(frame, np.ndarray):
        break

    imageName = os.path.join(root_path, str(i)+".jpg")
    cv2.imwrite(imageName, frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()