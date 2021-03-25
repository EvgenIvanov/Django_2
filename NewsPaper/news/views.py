# from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DeleteView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'