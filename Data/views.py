from _pydecimal import Decimal
import PIL
# import numpy as np
import pylab
from django.shortcuts import render
from django.http import HttpResponse
# import random
import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
# from matplotlib.dates import DateFormatter
from matplotlib import pyplot as plt, style
import io
from datetime import *
# from matplotlib.pyplot import figure, axes, plot, xlabel, ylabel, title, grid

DataFilePathTemperature = "D:/Rudra/VirtualEnv/WaterQualitySystem 2 - LIVE/Data/files/Temperature.txt"
DataFilePathConductivity = "D:/Rudra/VirtualEnv/WaterQualitySystem 2 - LIVE/Data/files/Conductivity.txt"
DataFilePathpH = "D:/Rudra/VirtualEnv/WaterQualitySystem 2 - LIVE/Data/files/pH.txt"
style.use("ggplot")


# Create your views here.


def index(request):
    context = {
        'image_name': 'Temperature Data',
        'image': 'D:/Rudra/VirtualEnv/WaterQualitySystem/images/image.jpeg'
    }
    return render(request, template_name='data/data.html', context=context)


def Last24HoursTemperature(request):
    style.use("ggplot")

    last24HoursFigureTemperature = Figure(figsize=(13, 6), dpi=100)
    pltLast24HoursTemperature = last24HoursFigureTemperature.add_subplot(111)

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
    canvas = FigureCanvas(last24HoursFigureTemperature)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def LastYearTemperature(request):
    lastYearFigureTemperature = Figure(figsize=(13, 6), dpi=100)
    pltLastYearTemperature = lastYearFigureTemperature.add_subplot(111)
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
            if interval.days <= 365:
                date, time = date.split(' ')
                xAxisDateTime = str(timestamp1.date().year) + " " \
                                + timestamp1.date().strftime('%b')
                xList.append(xAxisDateTime)
                yList.append(Decimal(temp))
                pltLastYearTemperature.clear()
                pltLastYearTemperature.set_title(str(timestamp1.date().year) + " Temperature Graph")
                pltLastYearTemperature.set_ylabel("Temperature (Degrees Celcius)")
                pltLastYearTemperature.set_xlabel("Month Wise Data ")

                pltLastYearTemperature.scatter(xList, yList, marker='.')
                lastYearFigureTemperature.autofmt_xdate()

    buffer = io.BytesIO()
    canvas = FigureCanvas(lastYearFigureTemperature)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def Last24HoursConductivity(request):
    last24HoursFigureConductivity = Figure(figsize=(13, 6), dpi=100)
    pltLast24HoursConductivity = last24HoursFigureConductivity.add_subplot(111)

    pullData = open(DataFilePathConductivity, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, cond = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 1:
                date, time = date.split(' ')
                hour, minute, second = time.split(':')
                xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                xList.append(xAxisDateTime)
                yList.append(Decimal(cond))

                pltLast24HoursConductivity.clear()
                pltLast24HoursConductivity.set_title(str(timestamp1.date().year) + " Conductivity Graph")
                pltLast24HoursConductivity.set_ylabel("Conductivity (uS/Cm)")

                pltLast24HoursConductivity.set_xlabel(" Hour Wise Data ")

                pltLast24HoursConductivity.scatter(xList, yList, marker='.')
                last24HoursFigureConductivity.autofmt_xdate()

    buffer = io.BytesIO()
    canvas = FigureCanvas(last24HoursFigureConductivity)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def LastYearConductivity(request):
    lastYearFigureConductivity = Figure(figsize=(13, 6), dpi=100)
    pltLastYearConductivity = lastYearFigureConductivity.add_subplot(111)

    pullData = open(DataFilePathConductivity, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'

    for eachLine in dataList:
        if len(eachLine) > 1:
            date, cond = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 365:
                date, time = date.split(' ')
                xAxisDateTime = str(timestamp1.date().year) + " " \
                                + timestamp1.date().strftime('%b')
                xList.append(xAxisDateTime)
                yList.append(Decimal(cond))
                pltLastYearConductivity.clear()
                pltLastYearConductivity.set_title(str(timestamp1.date().year) + " Conductivity Graph")
                pltLastYearConductivity.set_ylabel("Conductivity (uS/Cm)")

                pltLastYearConductivity.set_xlabel("Month Wise Data ")

                pltLastYearConductivity.scatter(xList, yList, marker='.')
                lastYearFigureConductivity.autofmt_xdate()

    buffer = io.BytesIO()
    canvas = FigureCanvas(lastYearFigureConductivity)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def Last24HourspH(request):

    last24HoursFigurePh = Figure(figsize=(13, 6), dpi=100)
    pltLast24HoursPh = last24HoursFigurePh.add_subplot(111)

    pullData = open(DataFilePathpH, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, ph = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 1:
                date, time = date.split(' ')
                hour, minute, second = time.split(':')
                xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                xList.append(xAxisDateTime)
                yList.append(Decimal(ph))
                pltLast24HoursPh.clear()

                pltLast24HoursPh.set_title(str(timestamp1.date().year) + " pH Graph")
                pltLast24HoursPh.set_ylabel("pH Value")
                pltLast24HoursPh.set_xlabel("Hour Wise Data ")

                pltLast24HoursPh.scatter(xList, yList, marker='.')
                last24HoursFigurePh.autofmt_xdate()

    buffer = io.BytesIO()
    canvas = FigureCanvas(last24HoursFigurePh)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def LastYearpH(request):

    lastYearFigurePh = Figure(figsize=(13, 6), dpi=100)
    pltLastYearPh = lastYearFigurePh.add_subplot(111)

    pullData = open(DataFilePathpH, "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    fmt = '%Y-%m-%d %H:%M:%S.%f'

    for eachLine in dataList:
        if len(eachLine) > 1:
            date, ph = eachLine.split(',')
            timestamp1 = datetime.strptime(date, fmt)
            timestamp2 = datetime.strptime(str(datetime.now()), fmt)
            interval = (timestamp2 - timestamp1)
            if interval.days <= 365:
                date, time = date.split(' ')
                xAxisDateTime = str(timestamp1.date().year) + " " \
                                + timestamp1.date().strftime('%b')
                xList.append(xAxisDateTime)
                yList.append(Decimal(ph))
                pltLastYearPh.clear()
                pltLastYearPh.set_title(str(timestamp1.date().year) + " pH Graph")
                pltLastYearPh.set_ylabel("pH Value")

                pltLastYearPh.set_xlabel("Month Wise Data ")

                pltLastYearPh.scatter(xList, yList, marker='.')
                lastYearFigurePh.autofmt_xdate()

    buffer = io.BytesIO()
    canvas = FigureCanvas(lastYearFigurePh)
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")