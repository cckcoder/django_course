from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Author


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ["title", "author", "date_created", "date_updated"]


admin.site.register(Post, PostAdmin)
admin.site.register(Author)

