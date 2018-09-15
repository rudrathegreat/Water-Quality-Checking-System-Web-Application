from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


def index(request):
    # return HttpResponse('HELLO FROM TESTING')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, template_name='posts/index.html', context=context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, template_name='posts/details.html', context=context)
