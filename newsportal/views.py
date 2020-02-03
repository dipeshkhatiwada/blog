from django.shortcuts import render
from blog.models import Blog


def about(request):
    return render(request, 'about.html')


def home(request):
    data = Blog.objects.all()
    context = {
        'blogs': data
    }
    return render(request, 'home.html', context)