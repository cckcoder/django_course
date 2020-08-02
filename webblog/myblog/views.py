from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post, Author

def show_text(request):
    obj = Post.objects.all()

    return render(request, 'myblog/home.html', {'context': obj})

def show_single_post(request, id):
    obj = Post.objects.get(id=id)

    return render(request, 'myblog/post-detail.html', {'post': obj})

def show_authors_table(request):
    obj = Author.objects.all()

    return render(request, 'myblog/authors.html', {'authors': obj})
