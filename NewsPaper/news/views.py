# from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from datetime import datetime

from .models import Post
from .filters import NewFilter

class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    # queryset = Post.objects.order_by('-id')
    ordering = ['-id']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.today()
        return context

class PostDetail(DeleteView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'