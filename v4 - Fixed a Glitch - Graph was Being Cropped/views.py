from _pydecimal import Decimal

import PIL
import numpy as np
import pylab
from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from matplotlib import pyplot as plt, style
import io
from datetime import *

# Create your views here.
from matplotlib.pyplot import figure, axes, plot, xlabel, ylabel, title, grid


def index(request):
    context = {
        'image_name': 'Temperature Data',
        'image': 'D:/Rudra/VirtualEnv/WaterQualitySystem/images/image.jpeg'
    }
    return render(request, template_name='data/data.html', context=context)


def graphTest(request):

    LARGE_FONT = ("Verdana", 16)
    MEDIUM_FONT = ("Verdana", 12)
    style.use("ggplot")
    DataFilePathTemperature = "D:/Rudra/VirtualEnv/WaterQualitySystem 2 - LIVE/Data/files/Temperature.txt"
    DataFilePathConductivity = "files/conductivity.txt"
    DataFilePathpH = "files/pH.txt"

    # Figures and plots for Temperature
    last24HoursFigureTemperature = Figure(figsize=(13, 6), dpi=100)
    pltLast24HoursTemperature = last24HoursFigureTemperature.add_subplot(111)
    lastYearFigureTemperature = Figure(figsize=(13, 6), dpi=100)
    pltLastYearTemperature = lastYearFigureTemperature.add_subplot(111)

    # Figures and plots for Conductivity
    last24HoursFigureConductivity = Figure(figsize=(13, 6), dpi=100)
    pltLast24HoursConductivity = last24HoursFigureConductivity.add_subplot(111)
    lastYearFigureConductivity = Figure(figsize=(13, 6), dpi=100)
    pltLastYearConductivity = lastYearFigureConductivity.add_subplot(111)

    # Figures and plots for pH
    last24HoursFigurePh = Figure(figsize=(13, 6), dpi=100)
    pltLast24HoursPh = last24HoursFigurePh.add_subplot(111)
    lastYearFigurePh = Figure(figsize=(13, 6), dpi=100)
    pltLastYearPh = lastYearFigurePh.add_subplot(111)

    pullData = open(DataFilePathTemperature, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, temp = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 1:
                date, time = date.split(' ')
                hour, minute, second = time.split(':')
                # xList.append(Decimal(hour))
                xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                xList.append(xAxisDateTime)
                yList.append(Decimal(temp))

                pltLast24HoursTemperature.clear()
                pltLast24HoursTemperature.set_title(str(timestamp1.date().year) + " Temperature Graph")
                pltLast24HoursTemperature.set_ylabel("Temperature (Degrees Celcius)")

                pltLast24HoursTemperature.set_xlabel("Hour Wise Data")

                pltLast24HoursTemperature.scatter(xList, yList, marker='.')
                last24HoursFigureTemperature.autofmt_xdate()

    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(last24HoursFigureTemperature)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")