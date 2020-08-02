from django.urls import path
from . import views

urlpatterns = [
    #path('url-name', function_name)
    path('', views.show_text),
    path('post/<int:id>', views.show_single_post),
    path('authors', views.show_authors_table)
]
