from django.shortcuts import render
from django.http import  HttpResponse

def show_text(request):
    #return HttpResponse("Hello, My First Django")
    return render(request, 'myblog/base.html')
