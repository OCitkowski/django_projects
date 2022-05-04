from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Note


# def index(request):
#     return HttpResponse('index')
#
# def topics(request):
#     return HttpResponse('topics')


def index(request):
    ''' Mane page'''
    return render(request, 'notebook/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def notes(request):
#     ''' notes list page'''
    tests = [1,2,3,4,5,6,7,8,9,10]
    notes = Note.objects.order_by('date_create')
    title = 'My notes +'

    context = {'notes': notes, 'tests': tests, 'title': title}
    return render(request, 'notebook/notes.html', context)