from django.urls import path
from . import views

urlpatterns = [
    #path('url-name', function_name)
    path('', views.show_text)
]