from dataclasses import field
from django import forms
from .models import Post, Comm

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'body']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comm
    fields = ['comment']