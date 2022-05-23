from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.forms import CharField
from tkinter import CASCADE

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  post_time = models.DateTimeField(default=timezone.now)
  body = models.TextField(default='')

class Comment(models.Model):
  body = models.TextField(default='')
  time = models.DateTimeField(default=timezone.now)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)