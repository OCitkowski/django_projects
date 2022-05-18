from django.urls import path
from .views import PostListView, DetailView, HomeTemplateView

app_name = 'blog_urls'
urlpatterns = [
    # ex: /blog
    path('', HomeTemplateView.as_view(), name='home'),
    path('', HomeTemplateView.as_view(), name='about'),
    path('', HomeTemplateView.as_view(), name='contact'),

    path('blogs/', PostListView.as_view(), name='blogs'),
    path('blog/<slug:category_slug>/', DetailView.as_view(), name='categories_page'),

]

