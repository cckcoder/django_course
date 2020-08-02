from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "date_created", "date_updated"]


admin.site.register(Post, PostAdmin)
