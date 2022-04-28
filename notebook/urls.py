"""Defines Url pattern for notebook"""
from django.urls import path
# from . import views
from notebook.views import index, topics

app_name = 'note'
urlpatterns = [
    # Mane page
    # path('', index, name='index'),
    #topics page
    path('topics/', topics, name='topics page'),
    ]
