# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:50:17 2021

@author: W-H
"""

# Open a PDF file.
# fp = open(r'D:\Code\ToolPy\pdf\05100200051151335343.pdf', 'rb')


import fitz
import os


def pyMuPDF_fitz(pdfPath, imagePath):
    print("imagePath="+imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 4
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if False:
            # 下面的这段代码就是想要从一页PDF的中心点为起点截取到右下角的区域，截取整张图的1/4.
            mat = fitz.Matrix(2, 2)                  # 在每个方向缩放因子2
            rect = page.rect                         # 页面的矩形
            mp = rect.tl + (rect.br - rect.tl) * 0.5  # 矩形的中心
            clip = fitz.Rect(mp, rect.br)            # 目标区域
            pix = page.getPixmap(matrix=mat, clip=clip)
        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建
        splitName = os.path.splitext(pdfPath)
        pdfName = os.path.split(splitName[0])[-1]
        print(pdfName)
        pix.writePNG(imagePath+'/'+'%s_images_%s.png' %
                     (pdfName, pg))  # 将图片写入指定的文件夹内


def getText():
    ifile = r'D:\Code\ToolPy\pdf\【招招出行-13.07元-1个行程】高德打车电子发票.pdf'
    doc = fitz.open(ifile)  # 打开文档
    for p in doc.pages():
        text3 = p.get_text()
        print(text3)


if __name__ == "__main__":
    if False:
        pdfPath = r'D:\Code\ToolPy\pdf\05100200051151335343.pdf'
        imagePath = r'D:\Code\ToolPy\pdf'
        pyMuPDF_fitz(pdfPath, imagePath)
    elif True:
        getText()
    else:
        pass
