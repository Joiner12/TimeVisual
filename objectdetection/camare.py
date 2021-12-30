# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:28:32 2021

@author: W-H
"""

# import numpy as np
import cv2
import time


def extrac_frame(video_file, *args, **kwargs):
    """从视频中读取帧

    参数
    ----------
    video_file : str
        视频文件地址

    返回值
    -------
    None
    """

    cap = cv2.VideoCapture(video_file)
    while (True):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
        else:
            print("视频读取完毕或者视频路径异常")
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        time.sleep(1)
    cap.release()
    cv2.destroyAllWindows()


def capture_camare_video():
    """获取摄像头数据流

    参数
    ----------
    None

    返回值
    -------
    None
    """
    cap = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc(*'MJPG')
    fps = 20.0
    frameSize = (640, 480)
    out = cv2.VideoWriter('video.avi', codec, fps, frameSize)
    print("按键Q-结束视频录制")
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    extrac_frame(r'WeChat_20211230162610.mp4')