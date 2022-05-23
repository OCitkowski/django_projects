from django.urls import path
from .views import PostListView, PostDetailView, PostCategoryListView,  HomeTemplateView, AboutTemplateView, ContactTemplateView

app_name = 'blog_urls'
urlpatterns = [
    # ex: /blog
    path('', HomeTemplateView.as_view(), name='home'),
    path('about', AboutTemplateView.as_view(), name='about'),
    path('contact', ContactTemplateView.as_view(), name='contact'),
    path('blogs/', PostListView.as_view(), name='blogs'),
    path('blogs/<slug:category_slug>/', PostCategoryListView.as_view(), name='categories_page'),
    path('blog/<slug:post_slug>/', PostDetailView.as_view(), name='post_page'),
]

