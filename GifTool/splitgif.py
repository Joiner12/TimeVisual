from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import os
from PIL import Image, ImageSequence
import cv2
import numpy as np


def file_selector():
    # 创建Tkinter窗口
    root = Tk()

    # 隐藏Tkinter窗口
    root.withdraw()

    # 设置初始目录为C:\Users\W-H\Desktop
    initial_dir = "C:/Users/W-H/Desktop/hhh"

    # 文件选择窗口，筛选*.gif作为可选择文件
    file_path = askopenfilename(
        initialdir=initial_dir, filetypes=[("GIF Files", "*.gif")]
    )
    # 显示所选择的文件路径
    try:
        1 / len(file_path)
    except:
        print("取消文件选择....")
    print("GIF文件:%s" % (file_path))
    return file_path


def split_gif(gif_file, *args_, **pargs):
    # 在gif同文件夹内新建同名文件夹
    folder_path, file_name = os.path.split(gif_file)
    sep_folder_path = f"{folder_path}/{os.path.splitext(file_name)[0]}"
    os.mkdir(sep_folder_path)
    if not os.path.isdir(sep_folder_path):
        return
    # 获取文件夹中所有的GIF文件

    # 分解每个GIF文件为单张图片
    gif_image = Image.open(gif_file)

    # 逐帧保存为单张图片
    for i, frame in enumerate(ImageSequence.Iterator(gif_image)):
        frame_path = f"{sep_folder_path}/frame_{i}.png"
        frame.save(frame_path, "PNG")
        # print(frame_path)
    # 显示完成消息
    print("已完成分解GIF为单张图片")
    return sep_folder_path, i


def classify_aHash(image1_path, image2_path):
    """
    平均哈希算法计算，相似度越高返回值越小
    """

    # 输入灰度图，返回hash
    def getHash(image):
        avreage = np.mean(image)
        hash = []
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i, j] > avreage:
                    hash.append(1)
                else:
                    hash.append(0)
        return hash

    # 计算汉明距离
    def Hamming_distance(hash1, hash2):
        num = 0
        for index in range(len(hash1)):
            if hash1[index] != hash2[index]:
                num += 1
        return num

    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    image1 = cv2.resize(image1, (32, 32))
    image2 = cv2.resize(image2, (32, 32))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    hash1 = getHash(gray1)
    hash2 = getHash(gray2)
    return Hamming_distance(hash1, hash2)


def calc_ssim(file_dir, frame_num, *args_, **pargs):
    """
    遍历计算图像帧相似度
    """
    print("图像帧相似度计算.....")
    ssim_matrix = np.zeros((frame_num, frame_num))
    for j in range(frame_num):
        base_pic = f"{file_dir}/frame_{j}.png"
        for k in range(frame_num):
            tar_pic = f"{file_dir}/frame_{k}.png"
            ssim_ = classify_aHash(base_pic, tar_pic)
            ssim_matrix[j, k] = ssim_

    return ssim_matrix


def depress(ssim_matrix, file_dir, frame_num):
    """
    通过比较相似度压缩图像帧
    """
    print("压缩文件......")
    files_ = list()
    frame_index = [x for x in range(frame_num)]
    for k in range(frame_num - 1):
        if ssim_matrix[k, k + 1] == 0:
            frame_index.pop(k)
    # if not ssim_matrix[-1 : frame_index[-1]] == 0:
    #     frame_index.append(frame_num - 1)
    # 将列表转换为集合，并找到交集
    common_elements = list(set(frame_index) & set([x for x in range(frame_num)]))
    non_common_elements = list(
        set([x for x in range(frame_num)]).symmetric_difference(set(frame_index))
    )
    # rename
    for k in common_elements:
        try:
            os.rename(f"{file_dir}/frame_{k}.png", f"{file_dir}/_a_frm{k},50.png")
            files_.append(f"{file_dir}/_a_frm{k},50.png")

        except OSError as e:
            print(f"文件重命名失败: {e}")

    # delete
    for j in non_common_elements:
        try:
            os.remove(f"{file_dir}/frame_{j}.png")
            print(f"{file_dir}/frame_{j}.png deleted successfully.")
        except OSError as e:
            print(f"Error deleting file: {e}")
    print("完成文件压缩")
    return files_


def main():
    print("GIF 分解压缩")
    file_gif = file_selector()
    file_dir, frame_num = split_gif(file_gif)
    ssim_matrix = calc_ssim(file_dir, frame_num)
    pic_files = depress(ssim_matrix, file_dir, frame_num)
    test_rbg(pic_files)


def test_rbg(file_, *args_, **pargs):
    from rembg import remove

    print("背景消除......")
    for pic_file in file_:
        file_in = Image.open(pic_file)
        file_out = remove(file_in)
        file_out.save(pic_file)
    print("完成!")


if __name__ == "__main__":
    main()
