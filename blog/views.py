from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Teg, Post, Category
from django.views.generic import ListView, DetailView


# from .forms import TopicForm, EntryForm


class PostList(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'main page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Main page'
        contex['categories'] = Category.objects.all()
        return contex

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class ShowPost(DetailView):
    model = Post
    template_name = 'blog/404.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))



