#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/29 4:31 AM
# @Author : maxu
# @Site : 
# @File : chart.py
# @Software: PyCharm
from pyecharts.charts import Bar


class Chart:
    def __init__(self):
        import sql
        self.home = ''
        self.sql = sql.Sql()
        datas = self.sql.getS_all()
        datan = self.sql.getN_all()

        self.prepare_dataS = []
        self.prepare_dataN = []

        self.time = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']
        self.add = []
        for data in datas:
            self.add.append(data['add'])
            self.prepare_dataS.append(
                [float(data['s2004']), float(data['s2005']), float(data['s2006']),
                 float(data['s2007']), float(data['s2008']), float(data['s2009']),
                 float(data['s2010']), float(data['s2011']), float(data['s2012']),
                 float(data['s2013'])])

        for data in datan:
            # add.append(data['add'])
            self.prepare_dataN.append(
                [float(data['s2004']), float(data['s2005']), float(data['s2006']),
                 float(data['s2007']), float(data['s2008']), float(data['s2009']),
                 float(data['s2010']), float(data['s2011']), float(data['s2012']),
                 float(data['s2013'])])

    def initHome(self):
        from pyecharts import options as opts
        from pyecharts.charts import Map

        res = [[], [], [], [], [], [], [], [], [], []]
        for i in range(10):
            for j in range(len(self.prepare_dataN[:-1])):
                row = self.prepare_dataN[:-1][j]
                res[i].append([self.add[j], row[i]])
            print(res[i])
        print(res[0])

        def map_base() -> Map:
            c = (
                Map()

                    .set_global_opts(title_opts=opts.TitleOpts(title="主页"),
                                     legend_opts=opts.LegendOpts(selected_mode='single'),
                                     visualmap_opts=opts.VisualMapOpts(max_=10000, is_piecewise=True),
                                     )
            )
            for i in range(10):
                c.add(self.time[i], res[i], "china")
            c.width = '1080px'
            c.height = '600px'
            return c

        map_base().render('static/html/home.html')

    def initChart1(self):
        from pyecharts import options as opts
        from pyecharts.charts import Boxplot

        def boxpolt_base() -> Boxplot:
            c = Boxplot()
            # print(add)
            c.width = '1080px'
            c.height = '600px'
            # c.set_global_opts(xaxis_opts=opts.AxisTickOpts(is_align_with_label=True),)
            c.set_series_opts(label_opts=opts.LabelOpts(rotate=45))

            c.add_xaxis(self.add[:-1])
            c.add_yaxis('水足迹强度', c.prepare_data(self.prepare_dataS[:-1]))

            # for i in range(len(prepare_data)):
            c.add_yaxis('水足迹数值', c.prepare_data(self.prepare_dataN[:-1]))
            c.set_global_opts(title_opts=opts.TitleOpts(title="盒须图"))
            return c

        boxpolt_base().render('static/html/chart1.html')

    def initChart2(self):
        from pyecharts import options as opts
        from pyecharts.charts import Bar

        def bar_base() -> Bar:
            c = (
                Bar()
                    .add_xaxis(self.time)
                    .set_global_opts(title_opts=opts.TitleOpts(title="水足迹强度"))
            )
            for i in range(len(self.add) - 1):
                c.add_yaxis(self.add[i], self.prepare_dataS[i], )
            c.set_global_opts(legend_opts=opts.LegendOpts(selected_mode='single'), )

            return c

        bar_base().render('static/html/chart2.html')

    def initChart3(self):

        from pyecharts import options as opts
        from pyecharts.charts import HeatMap

        def heatmap_base() -> HeatMap:
            value1 = []
            for i in range(len(self.add) - 1):
                for j in range(len(self.time)):
                    value1.append([self.add[i], self.time[j], self.prepare_dataS[i][j]])
            value2 = []
            for i in range(len(self.add) - 1):
                for j in range(len(self.time)):
                    value2.append([self.add[i], self.time[j], self.prepare_dataN[i][j]])

            c = (
                HeatMap()
                    .add_xaxis(self.add)
                    .add_yaxis("水足迹强度", self.time, value1)
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="热力图"),
                    visualmap_opts=opts.VisualMapOpts(
                        max_=max(max(self.prepare_dataS[i]) for i in range(len(self.prepare_dataS) - 1))),
                    # legend_opts=opts.LegendOpts(selected_mode='single')
                )
            )
            c.set_series_opts()
            return c

        heatmap_base().render('static/html/chart3.html')

    def initChart4(self):
        import pyecharts.options as opts
        from pyecharts.charts import Line

        def line_base() -> Line:
            c = (
                Line()
                    .add_xaxis(self.time)
                    .set_global_opts(title_opts=opts.TitleOpts(title="水足迹强度"),
                                     legend_opts=opts.LegendOpts(selected_mode='single'))
            )
            for i in range(len(self.add) - 1):
                c.add_yaxis(self.add[i], self.prepare_dataS[i])
            return c

        line_base().render('static/html/chart4.html')

    def initChart5(self):
        from pyecharts import options as opts
        from pyecharts.charts import Scatter

        def scatter_base() -> Scatter:
            c = (
                Scatter()
                    .add_xaxis(self.time)
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="水足迹数值"),
                    visualmap_opts=opts.VisualMapOpts(type_="size", max_=max(
                        max(self.prepare_dataN[i]) for i in range(len(self.prepare_dataN) - 1)), min_=0),
                    legend_opts=opts.LegendOpts(selected_mode='single')
                )
            )

            for i in range(len(self.add) - 1):
                c.add_yaxis(self.add[i], self.prepare_dataN[i])
            return c

        scatter_base().render('static/html/chart5.html')

    def initChart6(self):
        from pyecharts import options as opts
        from pyecharts.charts import Bar
        def bar_base() -> Bar:
            c = (
                Bar()
                    .add_xaxis(self.time).add_yaxis('', self.prepare_dataN[1], stack="stack1",
                                                    itemstyle_opts=opts.ItemStyleOpts(color='#FFFFFF',
                                                                                      color0='#000000'))

                    .set_global_opts(title_opts=opts.TitleOpts(title="水足迹数值"),
                                     legend_opts=opts.LegendOpts(selected_mode='single'))
            )
            for i in range(len(self.add) - 1):
                c.add_yaxis(self.add[i], self.prepare_dataN[i], stack="stack1", is_selected=False)

            return c

        bar_base().render('static/html/chart6.html')

    def initChart7(self):
        from pyecharts import options as opts
        def bar_stack1() -> Bar:
            c = (
                Bar()
                    .add_xaxis(self.time)
                    .set_series_opts(label_opts=opts.LabelOpts())
                    .set_global_opts(title_opts=opts.TitleOpts(title="水足迹数值"),
                                     )
            )
            for i in range(len(self.add) - 1):
                c.add_yaxis(self.add[i], self.prepare_dataN[i], stack="stack1")
            return c

        bar_stack1().render('static/html/chart7.html')


if __name__ == '__main__':
    c = Chart()
    c.initHome()
    # c.initChart1()
    # c.initChart2()
    # c.initChart3()
    # c.initChart4()
    # c.initChart5()
    # c.initChart6()
    # c.initChart7()
