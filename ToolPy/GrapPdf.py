# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:50:17 2021

@author: W-H
"""

import fitz
import os


def pyMuPDF_fitz(pdfPath, imagePath):
    if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
        os.makedirs(imagePath)  # 若图片文件夹不存在就创建
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rect = page.rect  # 页面的矩形
        # 目标图像区域-1
        x00 = rect.width * 1700 / 2494  #x0
        y00 = rect.y0  #y0
        x01 = rect.width  #x1
        y01 = rect.height * 350 / 1584  #y1
        clip = fitz.Rect(x00, y00, x01, y01)
        print(page.get_textbox(clip))
        # save picture
        if True:
            mat = fitz.Matrix(4, 4).prerotate(int(0))
            pix = page.getPixmap(matrix=mat, alpha=False, clip=clip)
            splitName = os.path.splitext(pdfPath)
            pdfName = os.path.split(splitName[0])[-1]
            pix.save(imagePath + '/' + '%s_images_%s_part1.png' %
                     (pdfName, pg))  # 将图片写入指定的文件夹内
            # print('save image:' + imagePath + '/' + '%s_images_%s_part1.png' %
            #       (pdfName, pg))
        # 目标图像区域-2
        x10 = rect.x0  #x0
        y10 = rect.height * 1050 / 1584  #y0
        x11 = rect.width  #x1
        y11 = rect.height * 1200 / 1584  #y1
        clip = fitz.Rect(x10, y10, x11, y11)
        print(page.get_textbox(clip))
        if True:
            mat = fitz.Matrix(4, 4).prerotate(int(0))
            pix = page.getPixmap(matrix=mat, alpha=False, clip=clip)
            splitName = os.path.splitext(pdfPath)
            pdfName = os.path.split(splitName[0])[-1]
            pix.save(imagePath + '/' + '%s_images_%s_part2.png' %
                     (pdfName, pg))  # 将图片写入指定的文件夹内
            # print('save image:' + imagePath + '/' + '%s_images_%s_part2.png' %
            #       (pdfName, pg))


if __name__ == "__main__":
    if True:
        # pdfPath = r'D:\Codes\TimeVisual\ToolPy\pdf\【招招出行-13.07元-1个行程】高德打车电子发票.pdf'
        # pdfPath = r'D:\Codes\TimeVisual\ToolPy\pdf\05100200051151335343.pdf'
        # pdfPath = r'D:\Codes\TimeVisual\ToolPy\pdf\曹操出行电子发票 (2).pdf'
        imagePath = r'D:\Codes\TimeVisual\ToolPy\pdf'
        pyMuPDF_fitz(r'D:\Codes\TimeVisual\ToolPy\pdf\曹操出行电子发票 (2).pdf',
                     imagePath)
        pyMuPDF_fitz(
            r'D:\Codes\TimeVisual\ToolPy\pdf\05100200051151335343.pdf',
            imagePath)
    else:
        pass
