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
