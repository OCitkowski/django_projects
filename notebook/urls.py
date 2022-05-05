"""Defines Url pattern for notebook"""
from django.urls import path, include
# from . import views
from notebook.views import index, notes

app_name = 'notebook'
urlpatterns = [
    # Mane page
    path('', index, name='index'),
    #topics page
    path('notes/', notes, name='notes'),

    ]
