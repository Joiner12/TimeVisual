# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 09:44:26 2021

@author: W-H
"""

 
import imageio
 
def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 1)

    return

def main_1():
    image_list = list()
    for k in range(1,8,1):
        image_temp = r'../pic/erase/erase'+('%02d')%(k)+'.png'
        image_list.append(image_temp)
        print(image_temp)
    gif_name = '../pic/erase/erase.gif'
    create_gif(image_list, gif_name)
 
if __name__ == "__main__":
    main_1()
    
