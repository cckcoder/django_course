from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post

def show_text(request):
    obj = Post.objects.all()
    return render(request, 'myblog/base.html', {'context': obj})
