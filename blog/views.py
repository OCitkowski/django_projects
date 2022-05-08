from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# from .models import Topic, Entry
# from .forms import TopicForm, EntryForm


def index(request):
    ''' Mane page'''
    # return render(request, 'daybook/index.html')
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):

    return HttpResponse(f'ou"re looking at question {question_id}')
