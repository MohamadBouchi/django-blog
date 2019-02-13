from django.shortcuts import render

posts = [
    {
        'author': 'author1',
        'title': 'title1',
        'content': 'content1',
        'date_posted': 'august 1, 2018'
    },
    {
        'author': 'author2',
        'title': 'title2',
        'content': 'content2',
        'date_posted': 'august 2, 2018'
    },
    {
        'author': 'author3',
        'title': 'title3',
        'content': 'content3',
        'date_posted': 'august 3, 2018'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'blog/about.html')
