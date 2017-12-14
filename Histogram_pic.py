#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cairo
import pycha.bar
import json
import sys
import time
import pycha.line
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )

def openjson():
    with open(os.getcwd()+'\\'+'data.txt', 'r') as f:
                lines=[]
                for i in  f.readlines():
                    decode_json = json.loads(i)
                    data=(decode_json['time'],decode_json['Native Heap Alloc'])
                    index= (data.__str__()).replace('u','')
                    lines.append(tuple(eval(index)))
                index= (lines.__str__()).replace('[','(').replace(']',')')
                result=tuple(eval(index))
    return result


def barChart(output, chartFactory):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1200, 600)#设置画布

    dataSet = (
        ('lines', [(i, l[1]) for i, l in enumerate(openjson())]),
        )

    options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(openjson())],
                'label': 'Run Time',
                'rotate': 5
            },
            'y': {
                'tickCount': 30,
                'rotate': 30,
                'label': 'Size',
                'showLines':True,
                'tickPrecision':2
            }
        },
        'background': {
            'chartColor': '#FFFFFF',#背景颜色
            'baseColor': '#ffffff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'red',#圆柱体颜色
            },
        },
        'legend': {
            'hide': True,
        },
        'padding': {
            'left': 0,
            'bottom': 0,
        },
        'title': 'App内存监控柱状图',
        'titleFont':'字体',
        'titleColor':'#444444',
        'titleFontSize':30
    }
    chart = chartFactory(surface, options)
    #chart = pycha.line.LineChart(surface,options)
    #设置图表类型
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png(output)

    return output

if __name__ == '__main__':

    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = '_meminfo.png'
    starttimestamps = time.strftime("%Y%m%d%H%M%S")
    print barChart(str(starttimestamps) + output, pycha.bar.VerticalBarChart)#设置横着或者竖着


