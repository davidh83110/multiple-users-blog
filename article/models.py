from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

from mdeditor.fields import MDTextField

class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = MDTextField()
    category = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()