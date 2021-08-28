# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:35:53 2021

@author: Peace4Lv
"""

from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts
from os import path


def DrawImage(imgUrl="../html/pic/horizontalLine.png"):
    image = Image(page_title="image")
    # check file exists
    if not path.isfile(imgUrl):
        imgUrl = r"https://gitee.com/RiskyJR/pic-bed/raw/master/comm-timeline-graphic-1024x380.png"
    image.add(
        src=imgUrl,
        # image align center should modify outside
        style_opts={"style": "margin-top: 20px;text-align: center;width:1800px;height:900px;"},
    )
    image.set_global_opts(
        title_opts=ComponentTitleOpts(title="Time Line")
    )
    image.render("../html/imageTest.html")
    print("horizontal line image finished...\n")
    return image


if __name__ == "__main__":
    DrawImage()
