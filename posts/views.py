from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts



def index(request):
    # return HttpResponse('HELLO FROM TESTING')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts,
        'stars': static('HomePage/stars.jpg'),
        'river': static('HomePage/river.jpg'),
        'rain': static('HomePage/drip-drop.jpg'),
        'cow': static('HomePage/cow.png'),
        'deakin': static('HomePage/deakin.png'),
        'crosswalk': static('HomePage/crosswalk.jpg'),
        'background': static('HomePage/background.jpg'),
        'mw': static('HomePage/mw.png'),
        'yprl': static('HomePage/yprl.png'),
        'rudra': static('HomePage/Rudra.png'),
        'logo': static('HomePage/satms.jpg')

    }

    return render(request, template_name='posts/index.html', context=context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post,
        'stars': static('HomePage/stars.jpg'),
        'river': static('HomePage/river.jpg'),
        'rain': static('HomePage/drip-drop.jpg'),
        'cow': static('HomePage/cow.png'),
        'deakin': static('HomePage/deakin.png'),
        'crosswalk': static('HomePage/crosswalk.jpg'),
        'background': static('HomePage/background.jpg'),
        'mw': static('HomePage/mw.png'),
        'yprl': static('HomePage/yprl.png'),
        'rudra': static('HomePage/Rudra.png'),
        'logo': static('HomePage/satms.jpg')

    }

    return render(request, template_name='posts/details.html', context=context)
