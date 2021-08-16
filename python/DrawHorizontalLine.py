from pyecharts import options as opts
from pyecharts.charts import Line, Scatter
import numpy as np
"""
函数:
    使用area方式画矩形
定义:
    drawRect(x_left: int = 0, y_button: int = 0,
             width: int = 2, height: int = 1, color='#FF98AA')
参数:
    x_left,x坐标(左下角)
    y_button,y坐标(左下角)
    width,宽
    height,高
输出:
    pyecharts,line
"""


def drawRect(x_left: int = 0, y_button: int = 0,
             width: int = 2, height: int = 1, color='#65CFD5'):
    x = np.linspace(start=x_left,stop=x_left+width,num=3)
    y1 = np.zeros([1,len(x)])+y_button
    y2 = y1+height
    x = x.tolist()
    y1=y1.tolist()[0]
    y2 = y2.tolist()[0]
    line1 = Line(init_opts=opts.InitOpts())
    line1.add_xaxis(x)
    line1.add_yaxis("b", y2, color=color, is_symbol_show=False,
                    areastyle_opts=opts.AreaStyleOpts(opacity=1, color=color))
    line1.add_yaxis("a", y1, color=color, is_symbol_show=False,
                    areastyle_opts=opts.AreaStyleOpts(opacity=1, color='white'))
    line1.set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                          yaxis_opts=opts.AxisOpts(is_show=False, min_=-5, max_=5))
    return line1


x = [a for a in range(10)]
y1 = [1 for z in range(10)]
y2 = [2 for z in range(10)]
y4 = [1.5 for z in range(10)]
line1 = drawRect()
line2 = drawRect(2, 0, 6, 1, 'red')
scatter = (
    Scatter()
    .add_xaxis(x)
    .add_yaxis("d", y4)
)
line1.overlap(scatter)
line1.overlap(line2)
line1.render("..//html//horizontalLine.html")
print("因为我不知道 下一辈子还是否能遇见你\n所以我今生才会那么努力 把最后的给你\n")
