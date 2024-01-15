# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:38:41 2023

@author: W-H
"""
import matplotlib.pyplot as plt


def regulator_characters():
    # 稳压器技术性能指标
    RUB_CNY = 1 / 12.845318
    serial_num = [
        "IS350",
        "IS550",
        "IS800",
        "IS1000",
        "IS1000RT",
        "IS1500",
        "IS1500RT",
        "IS2000",
        "IS2500",
        "IS3000",
        "IS3500",
        "IS5000",
        "IS5000RT",
        "IS7000",
        "IS7000RT",
        "IS8000",
        "IS10000",
        "IS10000RT",
        "IS12000",
        "IS12000RT",
        "IS20000",
    ]
    price = [
        7890,
        9640,
        12620,
        14540,
        20400,
        17250,
        23270,
        21070,
        24780,
        28640,
        31670,
        48130,
        54770,
        55940,
        65190,
        68300,
        76420,
        105980,
        91570,
        125230,
        136350,
    ]

    power = [
        350,
        550,
        800,
        1000,
        1000,
        1500,
        1500,
        2000,
        2500,
        3000,
        3500,
        5000,
        5000,
        7000,
        7000,
        8000,
        10000,
        10000,
        12000,
        12000,
        20000,
    ]
    phase = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # convertor = [
    #     {"serial": "IS350", "price": 7890, "power": 350, "phases": 1},
    #     {"serial": "IS550", "price": 9640, "power": 550, "phases": 1},
    #     {"serial": "IS800", "price": 12620, "power": 800, "phases": 1},
    # ]
    fig, ax1 = plt.subplots()
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体为黑体
    color = "tab:red"
    ax1.set_xlabel("型号")
    ax1.set_ylabel("售价/元", color=color)
    ax1.bar(
        range(len(serial_num)), [x * RUB_CNY for x in price], color=color, alpha=0.7
    )
    ax1.set_xticks(range(len(serial_num)))  # 设置X轴刻度
    ax1.set_xticklabels(serial_num, rotation=50)  # 设置X轴标签并旋转45度
    ax1.tick_params(axis="y", labelcolor=color)
    # ax1.set_yticks(range(0, 10610, 200))
    # 在折线上的点添加价格和标签注释
    for i, txt in enumerate(price):
        ax1.annotate(
            "{}".format(int(txt * RUB_CNY)),
            (i, price[i] * RUB_CNY),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            color=color,
        )

    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("功率/瓦", color=color)
    ax2.plot(range(len(serial_num)), power, color=color, marker="o")
    ax2.tick_params(axis="y", labelcolor=color)
    plt.title("IS官网型号和功率售价图")
    plt.grid(True, linestyle="--", color="gray", alpha=0.5)
    fig.tight_layout()
    plt.show()


def input_output_characters():
    # 输入电压值
    phase_voltage = 100  # 替换为实际的相位输入电压值
    line_voltage = 200  # 替换为实际的线路输入电压值

    # 额定输出功率
    rated_power = 1000  # 替换为实际的额定输出功率值

    # 根据条件计算输出功率
    if (135 < phase_voltage < 165) or (234 < line_voltage < 285):
        output_power = 0.2 * rated_power
    elif (90 < phase_voltage < 135) or (155 < line_voltage < 234):
        output_power = 0.4 * rated_power
    else:
        output_power = rated_power

    # 绘制柱状图
    labels = ["Rated Power", "Output Power"]
    values = [rated_power, output_power]

    plt.bar(labels, values)
    plt.ylabel("Power (W)")
    plt.title("Rated Power vs Output Power")
    plt.show()


if __name__ == "__main__":
    input_output_characters()
