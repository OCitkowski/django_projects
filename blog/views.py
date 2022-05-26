import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tag, Post, Category
from django.views.generic import ListView, DetailView, TemplateView
# from .forms import TopicForm, EntryForm
from .utils import MixinTemplateView, menu

# def redirect_view(request):
#     response = redirect('blogs/')
#     return response

class AboutTemplateView(MixinTemplateView, TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title = 'about', test = 'test')

        return context | user_context

class HomeTemplateView(MixinTemplateView, TemplateView):
    template_name = "blog/base.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title = 'home')

        return context | user_context

class ContactTemplateView(MixinTemplateView, TemplateView):
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title = 'contact')

        return context | user_context


class PostListView(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    # extra_context = {'title': 'main page'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Blogs page'
        context['blog_cats'] = Category.objects.all()
        context['blog_tags'] = Tag.objects.all()
        context['menu'] = menu
        first_posts = Post.objects.filter(status='p').order_by('-date_update')[:2]
        context['first_posts'] = first_posts
        context['months_of_year'] = set(post.date_added.strftime("%B %Y") for post in self.get_queryset())

        return context

    def get_queryset(self):
        return Post.objects.filter(status='p')


class PostCategoryListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'category_slug'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs page'
        context['blog_cats'] = Category.objects.all()
        context['blog_tags'] = Tag.objects.all()
        context['menu'] = menu

        first_posts = Post.objects.filter(status='p').order_by('-date_update')[:0]
        context['first_posts'] = first_posts

        return context


    def get_queryset(self):
        category_id = Category.objects.get(slug=self.kwargs['category_slug']).id
        queryset = Post.objects.filter(status='p', category=category_id).order_by('-date_added')

        return queryset


class PostTagListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'tag_slug'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs page'
        context['blog_cats'] = Category.objects.all()
        context['blog_tags'] = Tag.objects.all()
        context['menu'] = menu

        first_posts = Post.objects.filter(status='p').order_by('-date_update')[:0]
        context['first_posts'] = first_posts

        return context


    def get_queryset(self):
        tag_id = Tag.objects.get(slug=self.kwargs['tag_slug']).id
        queryset = Post.objects.filter(status='p', tag=tag_id).order_by('-date_added')

        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['categories'] = Category.objects.all()
        context['menu'] = menu

        return context



