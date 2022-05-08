from django.urls import path
from .views import PostsListAll, PostsListCategory

app_name = 'blog'
urlpatterns = [
    # ex: /topics
    path('', PostsListAll.as_view(), name='main page'),
    path('category/<slug:category_slug>/', PostsListCategory.as_view(), name='categories'),

]