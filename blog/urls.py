from django.urls import path
from .views import PostList, ShowPost

app_name = 'blog'
urlpatterns = [
    # ex: /topics
    path('', PostList.as_view(), name='main_page'),
    path('/<slug:category_slug>/', ShowPost.as_view(), name='categories_page'),
]