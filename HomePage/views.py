from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render


# Create your views here.

context = {
    'stars': static('HomePage/stars.jpg'),
    'river': static('HomePage/landscape.jpg'),
    'rain': static('HomePage/drip-drop.jpg'),
    'cow': static('HomePage/cow.png'),
    'deakin': static('HomePage/deakin.png'),
    'crosswalk': static('HomePage/crosswalk.jpg'),
    'background': static('HomePage/background.jpg'),
    'mw': static('HomePage/melbournew.png'),
    'yprl': static('HomePage/yprl.png'),
    'rudra': static('HomePage/Rudra.png'),
    'logo': static('HomePage/Logo.jpg'),
    'navCSS': static('HomePage/CSS/navbar.css'),
    'kangaroo': static('HomePage/kangaroo.jpg'),
    'socialIcons': static('HomePage/CSS/social-icons.css'),
    'fontawesome': static('HomePage/CSS/fontawesome/css/all.css'),
    'RMIT': static('HomePage/RMIT.png'),
    'rsv': static('HomePage/rsv.png'),
    'yf': static('HomePage/yf.png'),
    'ia': static('HomePage/ia.png'),
    'vsg': static('HomePage/vsg.png'),
    'lsc': static('HomePage/lsc.png'),
    'mu': static('HomePage/mu.png'),
    'wts': static('HomePage/wts.png'),
    'navbarJS': static('HomePage/JS/navbar.js')

}


def index(request):
    context['mainCSS'] = static('HomePage/CSS/homepage.css')
    context['slider'] = static('HomePage/CSS/slider.css')
    return render(request, template_name='HomePage/index.html', context=context)


def AboutUs(request):
    context['mainCSS'] = static('HomePage/CSS/aboutus.css')
    context['r3'] = static('HomePage/r3.jpg')
    return render(request, template_name='HomePage/AboutUs.html', context=context)


def WQCS(request):
    context['mainCSS'] = static('HomePage/CSS/WQCS.css')
    context['platypus1'] = static('HomePage/platypus1.jpg')
    context['platypus2'] = static('HomePage/platypus2.jpg')
    return render(request, template_name='HomePage/WQCS.html', context=context)


def HKWTS(request):
    context['mainCSS'] = static('HomePage/CSS/HKWTS.css')
    context['litter'] = static('HomePage/litter.jpg')
    context['robot'] = static('HomePage/r3.jpg')
    return render(request, template_name='HomePage/HKWTS.html', context=context)


def RUMS(request):
    context['mainCSS'] = static('HomePage/CSS/RUMS.css')
    context['tank'] = static('HomePage/tank.jpg')
    context['tank2'] = static('HomePage/wtank.jpg')
    return render(request, template_name='HomePage/RUMS.html', context=context)


def Contacts(request):
    context['mainCSS'] = static('HomePage/CSS/contacts.css')
    return render(request, template_name='HomePage/contacts.html', context=context)

def posts(request):
    message=''
    posts = 0
    if posts == 0:
        message = 'Sorry, There are Currently No Posts'
    context['mainCSS'] = static('HomePage/CSS/posts.css')
    context['message'] = message
    return render(request, template_name='HomePage/posts.html', context=context)

def showMonitoringDataPage(request):
    context['mainCSS'] = static('HomePage/CSS/data.css')
    return render(request, template_name='HomePage/data.html', context=context)

def tkp(request):
    context['mainCSS'] = static('HomePage/CSS/TKP.css')
    context['kangaroo1'] = static('HomePage/kangaroo1.jpg')
    context['kangaroo2'] = static('HomePage/kangaroo2.jpg')
    return render(request, template_name='HomePage/TKP.html', context=context)

def projects(request):
    context['mainCSS'] = static('HomePage/CSS/projects.css')
    return render(request, template_name='HomePage/projects.html', context=context)
