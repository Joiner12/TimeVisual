# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 08:55:16 2021

@author: W-H
"""

# -*- coding:utf-8 -*-
import queue
from concurrent.futures import ThreadPoolExecutor
import zipfile
import itertools


class BoundedThreadPoolExecutor(ThreadPoolExecutor):
    def __init__(self, max_workers=None, thread_name_prefix=''):
        super().__init__(max_workers, thread_name_prefix)
        self._work_queue = queue.Queue(self._max_workers * 2)  # 设置队列大小


def extract(file, password):
    if not flag:
        return
    file.extractall(path='.', pwd=''.join(password).encode('utf-8'))


def result(f):
    exception = f.exception()
    if not exception:
        # 如果获取不到异常说明破解成功
        print('密码为:', f.pwd)
        global flag
        flag = False


if __name__ == '__main__':
    # 创建一个标志用于判断密码是否破解成功
    flag = True
    # 创建一个线程池
    pool = ThreadPoolExecutor(100)
    nums = [str(i) for i in range(10)]
    upper_chrs = [chr(i) for i in range(65, 91)]
    lower_chrs = [chr(i) for i in range(97, 123)]
    # 尝试1-15位纯数字
    for k in range(1, 11, 1):
        if not flag:
            break
        print('尝试纯数字密码位数:%d' % (k+1))
        password_lst = itertools.permutations(nums, k)
        # 创建文件句柄
        zfile = zipfile.ZipFile(
            r"C:\Users\W-H\Desktop\python科学计算第二版_.zip", 'r')
        for pwd in password_lst:
            # print('try:', pwd)
            if not flag:
                break
            f = pool.submit(extract, zfile, pwd)
            f.pwd = pwd
            f.pool = pool
            f.add_done_callback(result)
    # 尝试6-10位数字+大小写字母
    for k in range(6, 11, 1):
        if not flag:
            break
        print('尝试纯数字+字母位数:%d' % (k))
        password_lst = itertools.permutations(nums+upper_chrs+lower_chrs, k)
        # 创建文件句柄
        zfile = zipfile.ZipFile(
            r"C:\Users\W-H\Desktop\python科学计算第二版_.zip", 'r')
        for pwd in password_lst:
            # print('try:', pwd)
            if not flag:
                break
            f = pool.submit(extract, zfile, pwd)
            f.pwd = pwd
            f.pool = pool
            f.add_done_callback(result)
