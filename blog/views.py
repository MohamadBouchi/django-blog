from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'blog/about.html')
