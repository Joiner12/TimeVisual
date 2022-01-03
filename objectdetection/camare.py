# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:28:32 2021

@author: W-H
"""

# import numpy as np
import cv2
import time


def test_camare(camare_num, *args, **kwargs):
    """测试摄像头

    参数
    ----------
    camare_num : int
        摄像头ID,笔记本电脑自带电脑为:0,外接设备为:1.

    返回值
    -------
    None
    """
    cap = cv2.VideoCapture(camare_num)
    print(cap.get(cv2.CAP_PROP_FPS))
    # cap.get()
    print("按键Q-结束测试")
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            print('摄像头打开失败')
    cap.release()
    cv2.destroyAllWindows()


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


def capture_motion_video():
    """获取变化摄像头数据流

    参数
    ----------
    None

    返回值
    -------
    None
    """
    cap = cv2.VideoCapture(1)
    codec = cv2.VideoWriter_fourcc(*'MJPG')
    fps = 20.0
    frameSize = (640, 480)
    out = cv2.VideoWriter('video.avi', codec, fps, frameSize)
    print("按键Q-结束视频录制")
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def average_hash(img, *args, **kwargs):
    """均值哈希算法,用以比较两图相似度

    参数
    ----------
    img : str
        图像文件

    返回值
    -------
    None
    """
    #缩放为8*8
    img = cv2.resize(img, (8, 8))
    #转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    #遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    #求平均灰度
    avg = s / 64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


if __name__ == "__main__":
    # extrac_frame(r'WeChat_20211230162610.mp4')
    # capture_motion_video()
    test_camare(1)