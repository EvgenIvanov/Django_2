# from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from datetime import datetime

from .models import Post
from .filters import NewFilter
from .forms import NewForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    ordering = ['-id']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.today()
        return context

    def get_absolute_url(self):
        return f'/news/{self.id}'

class PostDetail(DetailView):
    model = Post
    template_name = 'new_detail.html'
    context_object_name = 'new'
    queryset = Post.objects.all()

class PostCreate(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_add.html'
    form_class = NewForm

    def test_func(self):
        # obj = self.get_object()

        return self.request.user.groups.filter(name='authors').exists()

class PostUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'new_add.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def test_func(self):
        obj = self.get_object()
        return obj.author_id.user_id == self.request.user

class PostDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    success_url = '/news/'

    def test_func(self):
        obj = self.get_object()
        return obj.author_id.user_id == self.request.user
