# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:29:15 2021

@author: W-H
"""


import cv2
import numpy as np
import os
# PIL : Python Imaging Library
from PIL import Image
import re


class PicVideo():
    def __init__(self):
        pass

    def VideoToImage(self, videofile):
        # 导入所需要的库

        # 定义保存图片函数
        # image:要保存的图片名字
        # addr；图片地址与相片名字的前部分
        # num: 相片，名字的后缀。int 类型
        def save_image(image, addr, num):
            address = addr + str(num) + '.png'
            cv2.imwrite(address, image)

        # 读取视频文件
        videoCapture = cv2.VideoCapture(videofile)
        # fps = videoCapture.get(cv2.CAP_PROP_FPS)  # 获取帧率
        # width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
        # height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
        # suc = videoCapture.isOpened()  # 是否成功打开

        # 读帧
        success, frame = videoCapture.read()
        i = 0
        timeF = 4
        j = 0
        while success:
            i = i + 1
            if (i % timeF == 0):
                j = j + 1
                save_image(frame, './image/', j-1)
                print('save image:', i)
            success, frame = videoCapture.read()
        videoCapture.release()


def Png2Icon():
    inputimg = r'D:\Code\TimeVisual\python\image\1.png'
    thresh = 255

    img1 = cv2.imread(inputimg, 0)
    ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

    img = cv2.imread(inputimg)
    b, g, r = cv2.split(img)
    b[thresh1 > thresh] = 0
    g[thresh1 > thresh] = 0
    r[thresh1 > thresh] = 0
    alpha_channel = np.zeros(b.shape, dtype=b.dtype)
    alpha_channel[thresh1 < thresh] = 255

    img = cv2.merge([b, g, r, alpha_channel])
    cv2.imwrite("1.png", img)


def Pic2Icon(picfile, tarpath):
    size = (32, 32)
    # 分离文件名与扩展名
    [filepath, filename] = os.path.split(picfile)
    tmp = os.path.splitext(filename)
    # 因为python文件跟图片在同目录，所以需要判断一下
    if tmp[1] == '.png':
        outName = tmp[0] + '.ico'
        # 打开图片并设置大小
        # im = Image.open(picfile).resize(size)
        im = Image.open(picfile)
        try:
            # 图标文件保存至icon目录
            path = os.path.join(tarpath, outName)
            # im.save(path, format='ICO', sizes=[(32, 32)])
            im.save(path, format='ICO')

            print('{} --> {}'.format(picfile, outName))
        except IOError:
            print('connot convert :', picfile)


def CaputerGif(giffile, tarFolder):
    if not os.path.exists(tarFolder):
        os.mkdir(tarFolder)

# 常用格式图片保存为透明背景图片


def AlphaBackGround(PicFile):
    img = cv2.imread(PicFile)
    # cv2.imshow('src', img)
    # 让我们使用新的宽度和高度缩小图像
    down_width = 32
    down_height = 32
    down_points = (down_width, down_height)
    img = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
    # print(img.shape)

    result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    if True:
        for i in range(0, img.shape[0]):  # 访问所有行
            for j in range(0, img.shape[1]):  # 访问所有列
                if img[i, j, 0] > 200 and img[i, j, 1] > 200 and img[i, j, 2] > 200:
                    result[i, j, 3] = 0
        splitOut = os.path.split(PicFile)
        picName = os.path.splitext(splitOut[-1])
        # picName = os.path.join(splitOut[0], picName[0]+'_alpha'+'.png')
        newname = os.path.join(
            splitOut[0], r'light_monkey_'+str(picName[0])+'.png')
        cv2.imwrite(newname, result, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        Pic2Icon(newname, r'D:\Code\TimeVisual\python\icon')
        os.remove(newname)
        newname = os.path.join(
            splitOut[0], r'dark_monkey_'+str(picName[0])+'.png')
        cv2.imwrite(newname, result, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        Pic2Icon(newname, r'D:\Code\TimeVisual\python\icon')
        os.remove(newname)
    else:
        B, G, R = cv2.split(img)
        _, Alpha = cv2.threshold(R, 200, 255, cv2.THRESH_BINARY)
        cv2.imshow('thres', Alpha)

        B2, G2, R2, A2 = cv2.split(result)
        A2 = Alpha
        result = cv2.merge([B2, G2, R2, A2])  # 通道合并

        splitOut = os.path.split(PicFile)
        picName = os.path.splitext(splitOut[-1])
        picName = os.path.join(splitOut[0], picName[0]+'_alpha'+'.png')
        cv2.imwrite(picName, result)
    print(result.shape)
    # cv2.imshow('result', result)
    if False:
        B, G, R, A = cv2.split(result)
        cv2.imshow('B', B)
        cv2.imshow('G', G)
        cv2.imshow('R', R)
        cv2.imshow('A', A)
        cv2.waitKey()
    cv2.destroyAllWindows()

# convert rgb (224,224,3 ) to gray (224,224) image


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])  # 分别对应通道 R G B


def BatchRename():
    srcDir = r"C:\Users\W-H\Desktop\RunCat_for_windows-master\RunCat\resources\doge"
    tarDir = r"C:\Users\W-H\Desktop\RunCat_for_windows-master\RunCat\resources\catnew"
    files = os.listdir(srcDir)
    for pic in files:
        out = re.findall('\d{1,}', pic)
        oldname = os.path.join(srcDir, pic)

        if re.findall('light.*', pic):
            newname = os.path.join(
                tarDir, r'light_cat_'+str(int(out[0]))+'.png')
        else:
            newname = os.path.join(
                tarDir, r'dark_cat_'+str(int(out[0]))+'.png')
        os.rename(oldname, newname)
        print(oldname, out[0])


def BatchAlpha():
    pics = os.listdir(r'D:\Code\TimeVisual\python\image')
    for k in pics:
        AlphaBackGround(os.path.join(r'D:\Code\TimeVisual\python\image', k))

# 灰度图


def TransIntoGray(picfile, *pk, **pkw):
    img = cv2.imread(picfile)  # 读入图片
    Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 先要转换为灰度图片
    ret, thresh = cv2.threshold(
        Grayimg, 150, 255, cv2.THRESH_BINARY)  # 这里的第二个参数要调，是阈值！！

    cv2.imwrite('33.png', thresh)     # 存成一张图片！！！


if __name__ == "__main__":
    PicVideo().VideoToImage("aysao-e2vn1.gif")
    # BatchRename()
    BatchAlpha()
    # Pic2Icon(r'D:\Code\TimeVisual\python\33.png', r'D:\Code\TimeVisual\python')
    # TransIntoGray(r'D:\Code\TimeVisual\python\image\0.png')
