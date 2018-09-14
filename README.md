# Water Quality Checking System - Web Application
## Overview
### The Main Objective of this Project
#### The Overall Project

The aim of this project is to install smart water sensors into local areas known to be habitats for platypus. The will utilise environmental sensors connected to BBC Microbit which will allow the sensors to withdraw and store water quality information which is displayed nearby at signed stations. The signed stations will display the relevant information and act as a point where emergency information can be sent via 4G networks to relevant authorities. The equipment is to be designed utilising small-scale electronics powered by solar panels, as well as the BBC Microbit and E-waste which will allow for local students and community engagement. This allows the project to act as an educational tool that can raise awareness of Stormwater pollution.

##### The Sensing Component

This component sense the conductivity, pH and temperature values from the water on regular intervals.  It then sends this data to another BBC Microbit via radio signals. The sensing component is placed in the water and powered by solar panels to make it gain clean energy.

```Python

while True: 
    if uart.any():
        sleep(500)
        buffer = uart.readall()
        buf = str(buffer)

        if buf.find("cond") == 2:
            for i in buf:
                if i.isdigit() or i==".":
                    message = message + i
            message = "cond " + message
            radio.send(message)
            display.scroll(message, delay=50)
            buf = ""
            message = ""
            buffer = ""

        if buf.find("temp") == 2:
            for i in buf:
                if i.isdigit() or i==".":
                    message = message + i
            message = "temp " + message
            radio.send(message)
            display.scroll(message, delay=50)
            buf = ""
            message = ""
            buffer = ""

```

##### Radio Signal to Mobile Data Transmitter

Once data is received by the BBC MicroBit that is attached to an Arduino, The Arduino then transmits the data onto the 4G network, to make it available for further analysis. This component is attached to a display board which is located near a sidewalk close to the Plenty River. This board uses 4 LEDs indicators to show the water quality at a particular time. This  board also educates information about the platypuses which live in the river. This component also uses solar panels to get power.

Coloured LEDs will give an indication of water pollution. Large 10mm LEDs were connected to 180 ohm resistors.

> Red - Highly Polluted - connected to pin 12
>
> Orange - Bad - connected to pin 8
>
> Green - Good - connected to pin 16
>
> Blue - Excellent - connected to pin 0

The LEDs are connected to pins 12 and 8, and pins 16 and 0 of the BBC Micro:bit Motor Drive board Version2.

Pins 12 and 8 belong to one H Bridge Driver chip. Either pin 12 or pin 8 can be active (HIGH), but not both. Pins 16 and 0 belong to the second H Bridge Driver chip. Either pin 16 or pin 0 can be active (HIGH), but not both.

The board is designed to run motors (in pairs) and as such the pins are connected in pairs. The motor driver board uses a H Bridge driver chip, and as such if you try to run both pins at the same time the H bridge will automatically shut down to prevent damage.

##### Data Receiver and Storage Component

This component consists of a BBC Microbit that receives the data from cloud using 4G network and then pass that data to Raspberry Pi via serial port using decoder settings ‘UTF-8’. The Raspberry Pi process the data and save it in the data storage location. Data is stored in 3 separate data storage locations for pH, Conductivity and Temperature.

```Python

import serial
from time import sleep
import datetime
import os

PORT = '/dev/ttyACM0'
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

path = '/home/pi/Rudra/Files/Other/data.txt'
title = 'Temperature Recording System Data \n'
file_handle = open(path, 'w')
file_handle.write(title)
file_handle.close()

while True:
    data = s.readline().decode('UTF-8')
    temperature = data.rstrip().split(' ')

    print('Temp: ', temperature[0])
    present = datetime.datetime.now()
    print('Time: ', present)
    print('Day: ', present.day)
    print('Hour: ', present.hour)
    print('Minute: ', present.minute)
    print('Second: ', present.second)

    data_to_write = 'Temperature: ' + str(temperature[0]) + ' C' + '\n'\
                    + 'Date: ' + str(present.day)+ '/' + str(present.month) + '/' + str(present.year) + '\n'\
                    + 'Time: ' + str(present.hour) + ':' + str(present.minute) + ':' + str(present.second) + '\n'\
                    + '\n'

    try:
        file_handle = open(path, 'a')
        file_handle.write(data_to_write)
        file_handle.close()
    except:
        print('Error Uploading Data')

    sleep(1)
    
```

##### Water Quality Checking System - The Application that Graphs the Data

This application allows user to extract data from the database and process it using Matplotlib library to plot various graphs (Line, Pie, Scattered graphs etc.). The application process data in yearly and daily wise and allows user to view daily and yearly wise graphs for each data value (Temperature, Conductivity and pH). 

```Python

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
#import serial
from random import randint
import os.path
from datetime import *
from time import sleep
import matplotlib.dates as mdates

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
```

#### This Project

This web application allows user to view graphical data from anywhere using internet. The application extract data from the database and processes it using Matplotlib library to plot various graphs (Line, Pie, Scattered graphs etc.). The application process data in yearly and daily wise formats and allows user to view daily and yearly wise graphs for each data value (Temperature, Conductivity and pH).

```Python

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
from matplotlib import pyplot as plt
import io

# Create your views here.
from matplotlib.pyplot import figure, axes, plot, xlabel, ylabel, title, grid


def index(request):
    context = {
        'image_name': 'Temperature Data',
        'image': 'D:/Rudra/VirtualEnv/WaterQualitySystem/images/image.jpeg'
    }
    return render(request, template_name='data/data.html', context=context)


def graphTest(request):

    # Construct the graph
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)
    plot(t, s, linewidth=1.0)

    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)

    # Store image in a string buffer
    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")
    
```

#### Technologies Used
##### The Overall Project

> BBC Microbit
>
> Arduino
>
> Solar Panels
>
> Lithium Polymer Batteries
>
> Raspberry Pi
>
> Temperature, Conductivity and pH Sensors
>
> Python, Micropython, C
>
> Matplotlib, Django

##### This Project

> Python, Matplotlib, Django

### Setting Up the Environment

Before you start working on your Django project, you need all the reuqired applications, thus setting up the environment - 

```Bash

pip install virtualenv
pip install virtualenvwapper-win

mkvirtualenv name of environment
workon name of environment

pip install Django==2.1
python -mpip install -U matplotlib
pip install django-jinja

```

Then start a project - 

```Bash

django-admin startproject project name
cd project name

```

There is more information about Django, Matplotlib and Jinja below.

### Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

> Django was designed to help developers take applications from concept to completion as quickly as possible.
>
> Django takes security seriously and helps developers avoid many common security mistakes.
>
> Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

#### Designing Models

The data-model syntax offers many rich ways of representing your models – so far, it’s been solving many years’ worth of database-schema problems. Here’s a quick example - 

```Python

from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

```

Then run the Django command-line utility to create the database tables automatically - 

```Bash

python manage.py migrate

```

Once your models are defined, Django can automatically create a professional, production ready administrative interface – a website that lets authenticated users add, change and delete objects. It’s as easy as registering your model in the admin site - 

For `mysite/myapp/models.py` - 

```Python

from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

```

For `mysite/myapp/admin.py` - 

```Python

from django.contrib import admin

from . import models

admin.site.register(models.Article)

```

#### The URLs for Your Website

To design URLs for an app, you create a Python module called a URLconf. A table of contents for your app, it contains a simple mapping between URL patterns and Python callback functions. URLconfs also serve to decouple URLs from Python code.

Here’s what a URLconf might look like -

```Python

from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]

```

The code above maps URL paths to Python callback functions (“views”). The path strings use parameter tags to “capture” values from the URLs. When a user requests a page, Django runs through each path, in order, and stops at the first one that matches the requested URL. (If none of them matches, Django calls a special-case 404 view.)

#### Your Views

Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.

Generally, a view retrieves data according to the parameters, loads a template and renders the template with the retrieved data. Here’s an example view -

```Python

from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

```

#### The Templates

An example of it is - 

```html

{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}

``` 

This is where Jinja comes in.

Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment.

#### Running a Local Server

To run a test for you web project, simply - 

```Bash

python manage.py runserver

```

Make sure that when you are testing that `DEBUG` in `settings.py` is set to `TRUE`. When wanting to deploy your website, then set the value of `DEBUG` to `FALSE`.

### Matplotlib
#### Getting Started

> You can create a line plot with text labels using `plot()`
>
> Multiple axes (i.e. subplots) are created with the`subplot()` function
>
> Matplotlib can display images (assuming equally spaced horizontal dimensions) using the `imshow()` function
>
> The `pcolormesh()` function can make a colored representation of a two-dimensional array, even if the horizontal dimensions are unevenly spaced. The `contour()` function is another way to represent the same data
>
> The`hist()` function automatically generates histograms and returns the bin counts or probabilities
>
> You can add arbitrary paths in Matplotlib using the `matplotlib.path` module
>
> The mplot3d toolkit (see Getting started and 3D plotting) has support for simple 3d graphs including surface, wireframe, scatter, and bar charts.
>

#### More Complicated Stuff

`matplotlib.pyplot` is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that “axes” here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

Generating visualizations with pyplot is very quick:

```Python

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

```

to...

There are some instances where you have data in a format that lets you access particular variables with strings. For example, with `numpy.recarray` or `pandas.DataFrame`.

Matplotlib allows you provide such an object with the data keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.

```Python

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

```

#### Why Use Matplotlib

Matplotlib is a very efficient way
### Datetime
#### Using It

Python also has `datetime` which allows you to accurately get the time. If you want to find out what time it is, simply -

```Python

from datetime import *

present = datetime.datetime.now()
print(present)

```

You can also format it and compare them -

```Python
from datetime import datetime

pullData = open("sampleText.txt", "r").read()
dataList = pullData.split('\n')
xList = []
yList = []
fmt = '%Y-%m-%d %H:%M:%S.%f'
for eachLine in dataList:
    if len(eachLine) > 1:
        x, y = eachLine.split(',')
        timestamp1 = datetime.strptime(x, fmt)
        timestamp2 = datetime.strptime(str(datetime.now()), fmt)
        interval = (timestamp2 - timestamp1)
        if interval.days <= 1:
            date, time = x.split(' ')
            
```

You can find the present day, month, year, decade... simply type -

```Python

import datetime.datetime as present

print(present.day)
print(present.month)
print(present.minute)
print(present.second)
print(present.year)

```

And so on...

You can then use in Matplotlib on one of the axes. Copy as follows (if you want to do that) - 

**NOTE** - THIS IS NOT THE ENTIRE PART. IN ORDER FOR IT TO RUN, YOU NEED THE ENTIRE CODE (besides classes `PageOne` and `PageTwo` and the content in it). THIS IS ONLY THE BIT OF CODE WHICH PUTS THE DATES ON THE X-AXIS.

```Python

xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":" + str(timestamp1.minute)
xList.append(xAxisDateTime)
yList.append(int(y))
a.clear()
a.plot(xList, yList)
f.autofmt_xdate()

```

### More Information

> https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_canvas_sgskip.html
>
> https://matplotlib.org/tutorials/introductory/customizing.html#sphx-glr-tutorials-introductory-customizing-py
>
> https://matplotlib.org/tutorials/index.html
>
> https://matplotlib.org/
>
> https://www.python-course.eu/tkinter_buttons.php
>
> https://pypi.org/project/weather-api/
>
> https://github.com/PlatypusProject/Platypus-Monitoring-Project
>
> https://github.com/rudrathegreat/Water-Quality-Checking-System
>
> https://github.com/rudrathegreat/Microbit-Projects
>
> https://www.python.org
>
> https://docs.djangoproject.com/en/2.1/intro/overview/
> 
> https://www.youtube.com/watch?v=D6esTdOLXh4
>
> https://microbit.org/
>
> https://www.arduino.cc/
>
> http://jinja.pocoo.org/docs/2.10/
>
> https://www.djangoproject.com/

### Author

> Rudra
>
> https://github.com/rudrathegreat/

### News

> v1 - Got a Basic Non-Linear Graph On The Page
>
> v2 - Got a Basic Linear Graph On The Page
>
> v3 - Got Data From Data Storage Location Onto the Page
