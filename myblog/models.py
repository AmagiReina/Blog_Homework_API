from django.db import models


# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, default='Zhantuar')
    author_surname = models.CharField(max_length=255, default='Nupbayev')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


