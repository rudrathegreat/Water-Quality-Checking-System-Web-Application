from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

context = {
    'stars': static('stars.jpg'),
    'river': static('river.jpg'),
    'rain': static('drip-drop.jpg'),
    'cow': static('HomePage/cow.png'),
    'deakin': static('HomePage/deakin.png'),
    'crosswalk': static('crosswalk.jpg'),
    'background': static('background.jpg'),
    'mw': static('HomePage/mw.png'),
    'yprl': static('HomePage/yprl.png'),

}


def index(request):
    return render(request, template_name='HomePage/index.html', context=context)


def AboutUs(request):
    return render(request, template_name='HomePage/AboutUs.html', context=context)


def WQCS(request):
    return render(request, template_name='HomePage/WQCS.html', context=context)


def HKWTS(request):
    return render(request, template_name='HomePage/HKWTS.html', context=context)


def RUMS(request):
    return render(request, template_name='HomePage/RUMS.html', context=context)


def Contacts(request):
    return render(request, template_name='HomePage/contacts.html', context=context)

