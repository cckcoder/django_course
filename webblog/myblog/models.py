from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    feature_image = models.ImageField(upload_to="feature_photos")

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    job = models.CharField(max_length=40)
    profile_pic = models.ImageField(upload_to="profile_images")

    def __str__(self):
        return self.name
