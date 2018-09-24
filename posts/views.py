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

    return render(request, template_name='posts/index.html', context=context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post,
        'stars': static('posts/stars.jpg'),
        'river': static('posts/river.jpg'),
        'rain': static('posts/drip-drop.jpg'),
        'cow': static('posts/cow.png'),
        'deakin': static('posts/deakin.png'),
        'crosswalk': static('posts/crosswalk.jpg'),
        'background': static('posts/background.jpg'),
        'mw': static('posts/mw.png'),
        'yprl': static('posts/yprl.png'),

    }

    return render(request, template_name='posts/details.html', context=context)
