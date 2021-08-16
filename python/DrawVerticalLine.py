# -*- coding:utf-8 -*-
"""
    vertical event line
"""
import pyecharts.options as opts
from pyecharts.charts import Line
"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-sections

目前无法实现的功能:

1、visualMap 暂时无法设置隐藏
"""

x_data = [
    "00:00",
    "01:15",
    "02:30",
    "03:45",
    "05:00",
    "06:15",
    "07:30",
    "08:45",
    "10:00",
    "11:15",
    "12:30",
    "13:45",
    "15:00",
    "16:15",
    "17:30",
    "18:45",
    "20:00",
    "21:15",
    "22:30",
    "23:45",
]
y_data = [
    300,
    280,
    250,
    260,
    270,
    300,
    550,
    500,
    400,
    390,
    380,
    390,
    400,
    500,
    600,
    750,
    800,
    700,
    600,
    400,
]

(Line(init_opts=opts.InitOpts()).add_xaxis(
    xaxis_data=x_data).add_yaxis(
        series_name="用电量",
        y_axis=y_data,
        is_smooth=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="一天用电量分布", subtitle="纯属虚构"),
        tooltip_opts=opts.TooltipOpts(trigger="axis",
                                      axis_pointer_type="cross"),
        xaxis_opts=opts.AxisOpts(boundary_gap=False),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} W"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    ).set_series_opts(markarea_opts=opts.MarkAreaOpts(data=[
        opts.MarkAreaItem(name="早高峰", x=("07:30", "10:00")),
        opts.MarkAreaItem(name="晚高峰",
                          x=("17:30", "21:15"),
                          itemstyle_opts=opts.ItemStyleOpts(
                              color='green', opacity=0.8)),
    ])).render("..//html//verticallineTest.html"))
print("人生何其短 何必苦苦恋")