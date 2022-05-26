from .models import Tag, Post, Category
from django.views.generic import ListView, DetailView, TemplateView
from .utils import MixinView



class AboutView(MixinView, TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='about', test='test')

        return context | user_context


class HomeView(MixinView, TemplateView):
    template_name = "blog/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='home')

        return context | user_context


class ContactView(MixinView, TemplateView):
    template_name = "blog/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='contact')

        return context | user_context


class PostListView(MixinView, ListView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months_of_year'] = set(post.date_added.strftime("%B %Y") for post in self.get_queryset())
        user_context = self.get_user_context(title='blogs')
        return context | user_context

    def get_queryset(self):
        return Post.objects.filter(status='p')


class PostCategoryListView(MixinView, ListView):
    template_name = 'blog/index.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months_of_year'] = set(post.date_added.strftime("%B %Y") for post in self.get_queryset())
        user_context = self.get_user_context(title='blogs_category')
        return context | user_context

    def get_queryset(self):
        category_id = Category.objects.get(slug=self.kwargs['category_slug']).id
        queryset = Post.objects.filter(status='p', category=category_id).order_by('-date_added')

        return queryset


class PostTagListView(MixinView, ListView):
    template_name = 'blog/index.html'
    slug_url_kwarg = 'tag_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months_of_year'] = set(post.date_added.strftime("%B %Y") for post in self.get_queryset())
        user_context = self.get_user_context(title='blogs_tag')
        return context | user_context

    def get_queryset(self):
        tag_id = Tag.objects.get(slug=self.kwargs['tag_slug']).id
        queryset = Post.objects.filter(status='p', tag=tag_id).order_by('-date_added')

        return queryset


class PostDetailView(MixinView, DetailView):
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months_of_year'] = set(post.date_added.strftime("%B %Y") for post in self.get_queryset())
        user_context = self.get_user_context(title='blog')
        return context | user_context
