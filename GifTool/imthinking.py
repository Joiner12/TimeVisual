# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:48:47 2023

@author: W-H
"""


def _思考录():
    print("伪装成代码的思考录")


from tqdm import tqdm
from functools import wraps
import time


def progress_bar_decorator(desc="Progress", unit="item"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with tqdm(desc=desc, unit=unit, leave=False) as pbar:
                result = func(*args, progress_callback=pbar.update, **kwargs)

            return result

        return wrapper

    return decorator


# 使用装饰器
@progress_bar_decorator()
def example_function(progress_callback):
    total_iterations = 100  # 你可以在函数内部计算或者估算总迭代次数

    for _ in range(total_iterations):
        # 模拟函数内的某些操作
        time.sleep(0.1)  # 模拟耗时操作
        progress_callback(1)  # 更新进度条

        # 可以在进度条下方输出其他信息
        tqdm.write(f"Custom information: {_ + 1}/{total_iterations}")


# 调用被装饰的函数
# example_function()
with tqdm(total=200) as pbar:
    pbar.set_description("Processing:")
    # total表示总的项目, 循环的次数20*10(每次更新数目) = 200(total)
    for i in range(20):
        # 进行动作, 这里是过0.1s
        time.sleep(0.1)
        # 进行进度更新, 这里设置10个
        pbar.update(10)

import time, random

with tqdm() as p_bar:
    for i in range(50):
        # time.sleep(random.random())
        time.sleep(0.1)
        p_bar.update(1)
        p_bar.set_description("Processing {}-th iteration".format(i + 1))
