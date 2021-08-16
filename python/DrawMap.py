# -*- coding:utf-8 -*-
"""

1.机场数据
https://ourairports.com/data/

"""
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
import pandas as pd

extraPosition = {
    "多哈": (25.261101, 51.565102),
    "德黑兰": (35.7, 51.41666),
    "缅甸仰光": (16.77, 96.15),
    "芝加哥": (41.85, 87.683-180),
    "加德满都": (27.7, 85.3166667),
    "马德拉斯": (13.22, 81.33),
    "马德里": (40.43, 3.7),
    "邦达": (31.13, 97.18),
    "稻城亚丁": (29.323056, 100.053333),
    "新加坡樟宜": (1.36604863171, 104.003205457),
    "金边": (11.3623, 104.9154),
    "曼谷素万那普": (13.083, 100.483),
    "九寨黄龙": (32.85, 103.68),
    "孟买": (18.93, 72.85)
}


def DrawMap(FlightArrivalFile="..//data//FlightArrival.xlsx",
            FlightDepartureFile="..//data//FlightDeparture.xlsx"):
    # load data from excle
    ArrialInfo = pd.read_excel(FlightArrivalFile)
    DepartureInfo = pd.read_excel(FlightDepartureFile)
    FromCd = DepartureInfo['目的地'].to_list()
    ToCd = ArrialInfo['始发地'].to_list()
    FromCdD = dict()
    ToCdD = dict()
    for k in FromCd:
        if k in FromCdD.keys():
            FromCdD[k] += 1
        else:
            FromCdD[k] = 1

    for j in ToCd:
        if j in ToCdD.keys():
            ToCdD[j] += 1
        else:
            ToCdD[j] = 1
    geoData1 = list()
    geoData2 = list()
    geoData3 = list()
    testGeo = Geo()
    for k1, k2 in zip(FromCdD.keys(), FromCdD.values()):
        # lat[3.86 53.55]，lon[73.66 135.05]——中国
        try:
            a = testGeo.get_coordinate(k1)
            if a[1] >= 3.86 and a[1] <= 53.55:
                if a[0] >= 73.66 and a[0] <= 135.05:
                    geoData1.append((k1, k2))
                    geoData2.append(("成都双流", k1))
        except:
            pass

    for k1, k2 in zip(ToCdD.keys(), ToCdD.values()):
        try:
            if True:
                b = testGeo.get_coordinate(str(k1))
                if b[1] >= 3.86 and b[1] <= 53.55:
                    if b[0] >= 73.66 and b[0] <= 135.05:
                        geoData3.append((k1, "成都双流"))
            else:
                geoData3.append((k1, "成都双流"))
        except:
            pass

    geoAd = geoData2+geoData3

    c = Geo(init_opts=opts.InitOpts(width="900px", height="500px", page_title="Map-CDC",
            theme="light", bg_color="transparent"))
    # 添加其他位置
    for j in extraPosition.keys():
        c.add_coordinate(j, extraPosition[j][1], extraPosition[j][0])

    if False:
        c = (
            Geo(init_opts=opts.InitOpts(page_title="Map-CDC", bg_color="#2B3427"))
            .add_schema(maptype="china-cities")
            .add("geo", geoData1, color="blue", symbol_size=5)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="CDC"))
            .render("..//html//geoTest.html")
        )
    else:
        c.add_schema(maptype="china-cities")
        c.add("Destination", geoData1, type_=ChartType.EFFECT_SCATTER)
        c.add("Arrrial/Departure", geoAd, type_=ChartType.LINES,
              effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                          symbol_size=3,
                                          color="#475EEA"),
              linestyle_opts=opts.LineStyleOpts(curve=0.3, opacity=0.1, color="#5A98D4"))
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        c.set_global_opts(title_opts=opts.TitleOpts(title="Shuangliu Internatinal Airport",
                                                    subtitle="Chengdu"),
                          visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=50))
        c.render("..//html//geoTest.html")
    print("draw map run finished...\n")
    return c


if __name__ == "__main__":
    DrawMap(FlightArrivalFile="..//data//FlightArrival-2021-08-13.xlsx",
            FlightDepartureFile="..//data//FlightDeparture-2021-08-13.xlsx")
    # DrawMap()
