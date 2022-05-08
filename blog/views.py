from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Teg, Post, Category
from django.views.generic import ListView
# from .forms import TopicForm, EntryForm


class PostsListAll(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'main page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Main page'
        return contex

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostsListCategory(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'main page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Main page'
        return contex

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
