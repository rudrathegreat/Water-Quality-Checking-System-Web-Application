# Water Quality Checking System - Web Application
## Overview
### Project Description

Water resources are getting more and more important with each passing day in case of survival of humanity. For this reason, assessing water resources’ quality and also monitoring them have attracted lots of attention in the recent years. Remote sensing has been growing widely in the last decade and its resources are very usable when it comes to water resources management.

ONE of Victoria’s oldest platypuses calls the Plenty River home. The population of platypuses is reducing in the plenty river due to the rise in water pollution. 

The aim of this project is to install smart water sensors into local areas known to be habitats for platypus. The will utilise environmental sensors connected to BBC Microbit which will allow the sensors to withdraw and store water quality information which is displayed nearby at signed stations. The signed stations will display the relevant information and act as a point where emergency information can be sent via 4G networks to relevant authorities. The equipment is to be designed utilising small-scale electronics powered by solar panels, as well as the BBC Microbit and E-waste which will allow for local students and community engagement. This allows the project to act as an educational tool that can raise awareness of Stormwater pollution.

We know that good freshwater should have a conductivity value between 100 – 2000. Any higher than 10000 and it is then classified as industrial wastewater.

pH on the other hand works with 2 ends (0 and 14) with 7 in the middle as the neutral state. The pH scale shows how much acidic or basic something is. Water tends to be around 5.5 to 7.5. Higher than 8 and the pH scale shows artificial liquids.


### The Components

This component sense the conductivity, pH and temperature values from the water on regular intervals.  It then sends this data to another BBC Microbit via radio signals. The sensing component is placed in the water and powered by solar panels to make it gain clean energy.

```Python

from microbit import *
import radio
radio.config(length = 240, channel = 96)
radio.on()
sensor_status = ""
temp = ""
data = ""
count = 0
pin12.write_digital(0)
pin8.write_digital(0)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin2, rx=pin1)

def temp_on():
    pin12.write_digital(0)
    pin8.write_digital(1)   
    
def cond_on():
    pin12.write_digital(1)
    pin8.write_digital(0) 
    
while True:
    sleep(500)
    count += 1    
    if count >0 and count < 60:
        temp_on()
        sensor_status = "TEMP"
        display.show("T")
    if count > 60 and count < 120:
        cond_on()
        sensor_status = "COND"
        display.show("C")
    if count > 120:
        count = 0
     
    if uart.any():
        data=""
        buf=""
        buffer=""
        sleep(100)
        buffer = uart.readline()
        buf = str(buffer)
        for i in buf:
            if i.isdigit() or i==".":      #isdigit removes any non number based digits
                data = data + i
        if sensor_status == "TEMP" and count > 5:
            data = "T" + data
            radio.send(data)
            print(data)
        if sensor_status == "COND" and count > 65:
            data = "C" + data
            radio.send(data)     #this adds T for temperature before the data so the receiver knows what they got
            print(data)
            
 ```
 
 ##### UART on the Arduino
 
 UART on the Arduino uses two pins. One pin is set for tranmission (TX) the other is set for receiving (RX). When UART is connected to another device the pins must be crossed over. This means that the TX of one device must be connected to the RX of the second device, and vice versa.

The operating voltage of the two devices must also be considered. A 5V (e.g. Arduino Uno) can be connected to another 5V device.

If an 5V Arduino Uno is connected to a BBC Micro:bit (3.3V device) then a Digital Logic Converter is required between the two devices.

The UART serial communication on the Arduino in the Water Quality Sensor will be used to communicate to all the sensor probes (individually) and also to the BBC Micro:bit. As a result, each of these external devices will need two (2) dedicated Arduino pins.

Only one UART serial communication can be active at the one time. This is dictated by the SoftwareSerial library.

Each SoftwareSerial UART interface must be initialised by defining the pins that will be used for receiving (RX) and transmitting (TX) data. This is done by creating an object to represent the SoftwareSerial Class. The object in this instance is named - bbcSerial. An example of this initialition is - 

```C

SoftwareSerial bbcSerial(10, 11);       // RX - pin10, TX pin11
You also need to set the baud rate. This is done in the setup() block.

void setup() {                   //set up the hardware
  bbcSerial.begin(9600);        // set baud rate for BBC microbit connection 9600
}

```

To make the object bbcSerial active you need this code:

```C

bbcSerial.listen();            // Use listen method to turn on specific Software Serial port

```

**Example**

```C

//This code will output serial signals to a 5v-3V logic converter connected to a BBC Micro:bit
//Wiring - Arduino TX(yellow) to TXO on Logic Converter, Arduino RX(green) to RXI on Logic Converter

// Remember that the TX of the Arduino is connected to the RX of the BBC Micro:bit
// and the RX of the Arduino is connected to the TX of the BBC Micro:bit
// This is called a "cross-over" connection.

// Label all wires.

#include <SoftwareSerial.h>    //we have to include the SoftwareSerial library to support serial communcations

//define how the SoftwareSerial port is going to work
SoftwareSerial bbcSerial(10, 11);       // RX (green) is Arduino pin10, TX (yellow) is Arduino pin11 - BBC Microbit UART

String message = "hello";         //a string to hold the data for the message to the BBC micro:bit

void setup() {                   //set up the hardware
  bbcSerial.begin(9600);        // set baud rate for BBC microbit connection 9600
  bbcSerial.listen();            // Use listen method to turn on specific Software Serial port
}


void loop() {                          //here we go...
  bbcSerial.println(message);        // send data to BBC Microbit
  delay(5000); 
}

```

#### Radio Signal to Mobile Data Transmitter

Once data is received by the BBC MicroBit that is attached to an Arduino, The Arduino then transmits the data onto the 4G network, to make it available for further analysis.

This component is attached to a display board which is located near a sidewalk close to the Plenty River.

This board uses 4 LEDs indicators to show the water quality at a particular time. This  board also educates information about the platypuses which live in the river.

This component also uses solar panels to get power.

The Water Quality Sign has several functions:

> To receive sensory data from the Water Quality Probe
>
> To display the current water quality status for the stream using LEDs
>
> To transmit regular reports and alarm states as SMS text messages on the 4G network

The Water Quality Sign will be approximately 1050mm in height and 350mm in width. It will be mounted to a 3.6m x 125mm x 125mm Sawn
Cypress Post (Bunnings Australia). Two solar panels will be mounted at the top of the post. The post will be hollowed out behind the sign to house the electronics. The Aluminium signs (1050mm x 350mm) will be place on the front and back of the post.

One one side of the sign four coloured LEDs will be placed to give an indication of water quality. Water quality scale

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

For experimentation standard 3mm (diameter) LEDs were used. In the sign 10mm LEDs will be used (Jaycar). The LEDs are clear, but show their colour when illuminated.

```Python

def redLedOn():
    pin12.write_digital(1) 
    pin8.write_digital(0)  
    pin16.write_digital(0)
    pin0.write_digital(0)
    
def yellowLedOn():
    pin12.write_digital(0) 
    pin8.write_digital(1)  
    pin16.write_digital(0)
    pin0.write_digital(0)
 
def greenLedOn():
    pin12.write_digital(0) 
    pin8.write_digital(0)  
    pin16.write_digital(1)
    pin0.write_digital(0)

def blueLedOn():
    pin12.write_digital(0) 
    pin8.write_digital(0)  
    pin16.write_digital(0)
    pin0.write_digital(1)
    
def LedOff():
    pin12.write_digital(0) 
    pin8.write_digital(0)  
    pin16.write_digital(0)
    pin0.write_digital(0)
    
```

#### Data Receiver and Storage Component

This component consists of a BBC Microbit that receives the data from cloud using 4G network and then pass that data to Raspberry Pi via serial port using decoder settings ‘UTF-8’.

The Raspberry Pi process the data and save it in the data storage location. Data is stored in 3 separate respective data storage locations for pH, Conductivity and Temperature.

**Example**

```Python

'''This file will help you get
some dummy data to get working
with.'''

import datetime
from random import randint
from time import sleep

while True:

    temp = randint(150, 350)/10
    cond = randint(1100, 1450)
    pH = randint(300, 900)/100
    # Below is the part where the saving really happens
    path = 'files\sampleText.txt'
    file_handle = open(path, 'a')
    present = datetime.datetime.now()
    file_handle.write(str(present) + ',' + str(temp) + ',' + str(cond) + ',' + str(pH) + "\n")
    file_handle.close()
    sleep(20)

```

#### Water Quality Checking System - The Application that Graphs the Data

This application allows user to extract data from the database and process it using Matplotlib library to plot various graphs (Line, Pie, Scattered graphs etc.).

The application process data in yearly and daily wise and allows user to view daily and yearly wise graphs for each data value (Temperature, Conductivity and pH). 

**Example**

```Python

from _pydecimal import Decimal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk
from datetime import *
import matplotlib
from matplotlib import style

matplotlib.use("TkAgg")

LARGE_FONT = ("Verdana", 16)
MEDIUM_FONT = ("Verdana", 12)
style.use("ggplot")
DataFilePathpH = "files/pH.txt"

# Figures and plots for pH
last24HoursFigurePh = Figure(figsize=(5, 5), dpi=100)
pltLast24HoursPh = last24HoursFigurePh.add_subplot(111)
lastYearFigurePh = Figure(figsize=(5, 5), dpi=100)
pltLastYearPh = lastYearFigurePh.add_subplot(111)

def animateLast24HoursPh(i):
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


def animateLastYearPh(i):
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


class DataApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Water Quality Checking System")
        # receiveAndUpdateDataInFile()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=1)
        temperatureMenu = tk.Menu(menubar, tearoff=1)
        conductivityMenu = tk.Menu(menubar, tearoff=1)
        phMenu = tk.Menu(menubar, tearoff=1)
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Temperature Data", menu=temperatureMenu)
        temperatureMenu.add_command(label="Last 24 Hours",
                                    command=lambda: self.show_frame(HourlyGraphTemperature))
        temperatureMenu.add_separator()
        temperatureMenu.add_command(label="Last Year",
                                    command=lambda: self.show_frame(MonthlyGraphTemperature))
        menubar.add_cascade(label="Conductivity Data", menu=conductivityMenu)
        conductivityMenu.add_command(label="Last 24 Hours",
                                     command=lambda: self.show_frame(HourlyGraphConductivity))
        conductivityMenu.add_separator()
        conductivityMenu.add_command(label="Last Year",
                                     command=lambda: self.show_frame(MonthlyGraphConductivity))
        menubar.add_cascade(label="pH Data", menu=phMenu)
        phMenu.add_command(label="Last 24 Hours", command=lambda: self.show_frame(HourlyGraphPh))
        phMenu.add_separator()
        phMenu.add_command(label="Last Year", command=lambda: self.show_frame(MonthlyGraphPh))

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (
                StartPage, HourlyGraphPh, MonthlyGraphPh):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="WATER QUALITY CHECKING SYSTEM", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        label2 = tk.Label(self,
                          text="To check or monitor Temperature Or Conductivity Or pH Data,\n Please select graph option from menubar ",
                          font=MEDIUM_FONT)
        label2.pack(pady=30, padx=10)

        self.imageConductivityPh = tk.PhotoImage(file="files\ConductivityAndPh.gif")
        imageLabelConductivityPh = tk.Label(self, image=self.imageConductivityPh)
        imageLabelConductivityPh.pack(pady=0, padx=10)


class MonthlyGraphPh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last Year pH Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(lastYearFigurePh, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class HourlyGraphPh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Last 24 Hours pH Data ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        canvas = FigureCanvasTkAgg(last24HoursFigurePh, self)

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = DataApp()
app.geometry("1280x720")
# Animations for pH
ani5 = animation.FuncAnimation(last24HoursFigurePh, animateLast24HoursPh, interval=60000, blit=False)
ani6 = animation.FuncAnimation(lastYearFigurePh, animateLastYearPh, interval=60000, blit=False)
app.mainloop()

```

#### This Application

This web application allows user to view graphical data from anywhere using internet.
The application extract data from the database and process it using Matplotlib library to plot various graphs (Line, Pie, Scattered graphs etc.).
The application process data in yearly and daily wise and allows user to view daily and yearly wise graphs for each data value (Temperature, Conductivity and pH). 

Check it out here - https://mplsustainabilitysystems.herokuapp.com

**Example**

```Python

import matplotlib
matplotlib.use('Agg')
import PIL
import pylab
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt, style
import io
from datetime import *
from django.contrib.staticfiles.templatetags.staticfiles import static

DataFilePathTemperature = os.path.join(os.path.dirname(__file__), './files/Temperature.txt')
DataFilePathConductivity = os.path.join(os.path.dirname(__file__), './files/Conductivity.txt')
DataFilePathpH = os.path.join(os.path.dirname(__file__), './files/pH.txt')
style.use("ggplot")

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
    
```

### VirtualEnv

Virtualenv is a tool to create isolated Python environments.

The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you install everything into /usr/lib/python2.7/site-packages (or whatever your platform’s standard location is), it’s easy to end up in a situation where you unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be? If an application works, any change in its libraries or the versions of those libraries can break the application.

Also, what if you can’t install packages into the global site-packages directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that has its own installation directories, that doesn’t share libraries with other virtualenv environments (and optionally doesn’t access the globally installed libraries either).

##### Installation

To install globally with pip (if you have pip 1.3 or greater installed globally) - 

```Shell

pip install virtualenv

```

Or to get the latest unreleased dev version:

```Shell

pip install https://github.com/pypa/virtualenv/tarball/master

```

#### VirtualEnv-Wrapper

virtualenvwrapper is a set of extensions to Ian Bicking’s virtualenv tool. The extensions include wrappers for creating and deleting virtual environments and otherwise managing your development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies.

##### Installation

For Windows - 

```Shell

pip install virtualenvwapper-win

```

For any other OS - 

```Shell

pip install virtualenvwrapper

```

#### Creating a Virtual Environment

Simply -

```Shell

mkvirtualenv name

```

#### Switch Between or Work On a Virtual Environment(s)

Simply - 

```Shell

workon env1
workon env2

```

### Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

#### Installation

1. Install pip. Pip is now a part of Python 3. The easiest is to use the standalone pip installer. If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.

2. Install VirtualEnv and VirtualEnv-Wrapper. Then create a virtual environment.

3. After you’ve created and activated a virtual environment, enter the command `pip install Django` at the shell prompt.

If you’d like to be able to update your Django code occasionally with the latest bug fixes and improvements, follow these instructions -

1. Make sure that you have Git installed and that you can run its commands from a shell. (Enter `git help` at a shell prompt to test this.)

2. Check out Django’s main development branch -

```Shell

git clone https://github.com/django/django.git

```

This will create a directory django in your current directory.

3. Make sure that the Python interpreter can load Django’s code. The most convenient way to do this is to use virtualenv, virtualenvwrapper, and pip. The contributing tutorial walks through how to create a virtualenv.

After setting up and activating the virtualenv, run the following command - 

```Shell

pip install -e django/

```

#### Creating a Project

Simply - 


```Shell

django-admin startproject project-name

```

#### Creating an app Inside Your Project

Simply - 

```Shell

python manage.py startapp app-name

```

Add your app to your settings.py file to make sure it is part of the project - 

```Python

INSTALLED_APPS = [
  'app-name',
]

```

#### Creating Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

The basics - 

> Each model is a Python class that subclasses django.db.models.Model.
>
> Each attribute of the model represents a database field.
>
> With all of this, Django gives you an automatically-generated database-access API

**Example**

```Python

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
```

Then add your model to your database. Following the example above - 

```Shell

python manage.py makemigrations Person
python manage.py migrate

```

If you want to register your model in the admin page, then simply do this in `admin.py` - 

```Python

from django.contrib import admin
from .models import Posts
# Register your models here.

admin.site.register(Person)

```

#### Adding Urls

Simply do this in `urls.py` - 

```Python

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name='Home Page'),
]

```

#### Your Views

We now have to create `index` from the previous example in our `views.py`. Simply -

```Python

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  
  context = {
    'something' : 'something',
    }

  # return HttpResponse('Hello World')
  return render(request, template_name='HomePage/index.html', context=context)
  
```

#### Your HTML and CSS Templating

Now we have to create a `index.html` in our project inside `templates/HomePage`. This is because all templates (HTML Code) must be in this folder inside the app called `templates`. It is also a good idea to make a folder inside templates called the app-name which you are in. This is because Django registers all `templates` folders in your project and merges them into one while you run the server. if you do not have this `app-name` folder, then Django will get confused, especially when you have a lot of `index.html` files in your project.

**Example**

```HTML

    <div class="img-container">
        <nav>
            <ul>
                <img src="{{ logo }}" width="100" height="100">
                <li ><a href="/" >Home</a></li>
                <li ><a href="#" >About</a>
                <ul>
                    <li><a href="/about-us/">Meet the Team</a></li>
                </ul>
                </li>
                <li ><a href="#" >Projects</a>
                    <ul class="long-menu">
                        <li><a href="/wqcs/">Water Quality Checking System</a></li>
                        <li><a href="/rums/">Rainwater Usage Monitoring System</a></li>
                        <li><a href="/hkwts/">Helping Kids Walk to School</a></li>
                    </ul>
                </li>
                <li ><a href="#" >Monitoring Data</a>
                <ul>
                    <li><a href="#" class="submenu">Temperature</a>
                    <ul>
                        <li><a href="/data/last24HoursTemperature/" target="_blank">Last 24 Hours</a></li>
                        <li><a href="/data/lastYearTemperature/" target="_blank">Last Year</a></li>
                    </ul>
                    </li>
                    <li><a href="#" class="submenu">Conductivity</a>
                    <ul>
                        <li><a href="/data/last24HoursConductivity/" target="_blank">Last 24 Hours</a></li>
                        <li><a href="/data/lastYearConductivity/" target="_blank">Last Year</a></li>
                    </ul>
                    </li>
                    <li><a href="#" class="submenu-2">pH</a>
                    <ul>
                        <li><a href="/data/last24HourspH/" target="_blank">Last 24 Hours</a></li>
                        <li><a href="/data/lastYearpH/" target="_blank">Last Year</a></li>
                    </ul>
                    </li>
                </ul>
                </li>
                <li ><a href="#" >Contact Us</a>
                <ul>
                    <li><a href="/posts/">Post Feeds</a></li>
                    <li><a href="/contacts/">Contacts</a></li>
                </ul>
                </li>
                <li ><a href="/admin" target="_blank" >Admin</a></li>
            </ul>
        </nav>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <BR>
        <h1>Monitoring Data</h1>
        <br>
        <h2>LIVE Temperature, Conductivtity and pH Data Extracted from the Plenty River</h2>
        <br>
        <a class="btn" href="../">BACK TO HOME</a>
        <br>
        <br>
        <br>
        <br>
    </div>

```

##### Jinja Templating

Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:

**Example**

```HTML

<title>{% block title %}{% endblock %}</title>
<ul>
{% for user in users %}
  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
</ul>

```

#### Deploying on Heroku

Deploying on Heroku is relatively straightforward.

1. Create an acoount
2. Create a project and pipeline
3. Connect this pipeline to your Django Project on Github
4. Create a `runtime.txt` in your project

Your `runtime.txt` should look like this -

```

python-3.7.0

```

It basically mentions your Python Version.

5. Create a `requirements.txt`.

Your `requirements.txt` should look like this -

```

cycler==0.10.0
dj-database-url==0.5.0
Django==2.1
django-heroku==0.3.1
django-jinja==2.4.1
gunicorn==19.9.0
image==1.5.25
Jinja2==2.10
kiwisolver==1.0.1
MarkupSafe==1.0
matplotlib==2.2.3
numpy==1.15.1
Pillow==5.2.0
psycopg2==2.7.5
pyparsing==2.2.0
python-dateutil==2.7.3
pytz==2018.5
six==1.11.0
whitenoise==4.1

```

You can also make it from the shell or command line. Simply -

```Shell

pip freeze > requirements.txt

```

6. Deploy!

### Matplotlib

Matplotlib and most of its dependencies are all available as wheel packages for macOS, Windows and Linux distributions:

```Shell

python -mpip install -U pip
python -mpip install -U matplotlib

```

If you are using Python 2.7 on a Mac you may need to do:

```Shell

xcode-select --install

```

#### Getting Started

> You can create a line plot with text labels using plot()
> 
> Multiple axes (i.e. subplots) are created with thesubplot() function
> 
> Matplotlib can display images (assuming equally spaced horizontal dimensions) using the imshow() function
> 
> The pcolormesh() function can make a colored representation of a two-dimensional array, even if the horizontal dimensions are unevenly spaced. The contour() function is another way to represent the same data
> 
> Thehist() function automatically generates histograms and returns the bin counts or probabilities
> 
> You can add arbitrary paths in Matplotlib using the matplotlib.path module
> 
> The mplot3d toolkit (see Getting started and 3D plotting) has support for simple 3d graphs including surface, wireframe, scatter, and bar charts.
>
> etc.

#### More Complicated Stuff

`matplotlib.pyplot` is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that “axes” here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis.

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

#### Save it Onto a Buffer

To save it onto a buffer, simply - 

```Python

import os
from _pydecimal import Decimal

import matplotlib
matplotlib.use('Agg')
import PIL
import pylab
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt, style
import io
from datetime import *
from django.contrib.staticfiles.templatetags.staticfiles import static

buffer = io.BytesIO()
canvas = FigureCanvas(last24HoursFigureTemperature)
canvas.draw()
pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
pilImage.save(buffer, "PNG")
pylab.close()

```

### Intro to Tkinter
#### Make a Window

To make a window, call Tkinter and then use Tk() to make a window, then add Tk.mainloop() to keep the window up and running.

```Python

from tkinter import *

root = Tk()
root.mainloop()

```

#### Making a Text Box

Using root, we can make a text box. We just have to tell the text box which window to be in -

```Python

from tkinter import *

root = Tk()
Box = Text(root, width = 300, height = 500)
Box.pack()

root.mainloop()

```

#### Making a Button

To make a button, simply -

```Python

from tkinter import *

root = Tk()
button = Button(root, text = 'Quit', command = master.quit)
button.pack()

root.mainloop()

```

#### Integrating Matplotlib into Tkinter

In order to put a graph in a Tkinter window, we need to use a backend called `TkAgg`. Then we simply make the graph and put it onto a canvas - 

```Python

import matplotlib as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo

# Create a canvas
w, h = 300, 200
window = tk.Tk()
window.title("A figure in a canvas")
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()

# Generate some example data
X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)

# Create the figure we desire to add to an existing canvas
fig = mpl.figure.Figure(figsize=(2, 1))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig_x, fig_y = 100, 100
fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
canvas.create_text(200, 50, text="Zero-crossing", anchor="s")

# Let Tk take over
tk.mainloop()

```

### Intro to Os

Os is used to save files. To save some text into a file, simply -

```Python

import os.path

text = 'Hi my name is John!'
path = 'D:\John\Documnts\file.txt'

file_handle = open(path, 'a') # a means to append. w means to overwrite
file_handle.write(text)
file_handle.close()

```

### Datetime

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

You can find the present day, month, year, decade... simply -

```Python

import datetime.datetime.now as present

print(present.day)
print(present.month)
print(present.minute)
print(present.second)
print(present.year)

```

And so on...

## Further References

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
> https://github.com/rudrathegreat
> 
> https://www.python.org
> 
> https://www.djangoproject.com/
> 
> https://virtualenvwrapper.readthedocs.io/en/latest/
> 
> https://virtualenv.pypa.io/en/stable/
> 
> https://www.youtube.com/watch?v=D6esTdOLXh4
> 
> https://www.heroku.com
> 
> http://jinja.pocoo.org/docs/2.10/
> 
> https://tutorial-extensions.djangogirls.org/en/heroku/
> 
> https://pythonprogramming.net/creating-main-menu-tkinter/?completed=/customizing-tkinter-matplotlib-graph/
> 
> https://pythonprogramming.net/
> 
> https://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html

## News

Final Version - Edited Some Stuff in the templates

v6 - Finally got it working on Heroku

v5 - Updated Navigation System

v4 - Added Posts Section

v3 - Multiple Linear Graphs on Website

v2 - Finally Got Linear Graphs Working

v1 - Non-Linear Graph on Page

Thanks for Reading!
--------------------------------------------
