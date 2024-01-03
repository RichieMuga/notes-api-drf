from django.db import models

# Create your models here.
class Note(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)