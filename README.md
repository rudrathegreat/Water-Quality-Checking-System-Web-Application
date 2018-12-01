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

```Python

print('Good Bye!')

```
