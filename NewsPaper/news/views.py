# from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post
from datetime import datetime

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.today()
        return context

class PostDetail(DeleteView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'