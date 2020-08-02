from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
