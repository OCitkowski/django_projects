from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Teg, Post, Category
from django.views.generic import ListView, DetailView, TemplateView
# from .forms import TopicForm, EntryForm
from .utils import menu

# def redirect_view(request):
#     response = redirect('blogs/')
#     return response

class AboutTemplateView(TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

class HomeTemplateView(TemplateView):
    template_name = "blog/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

class ContactTemplateView(TemplateView):
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class PostListView(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'main page'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs page'
        context['blog_cats'] = Category.objects.all()
        context['blog_tags'] = Teg.objects.all()
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/404.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context



