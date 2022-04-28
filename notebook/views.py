from django.shortcuts import render
from django.shortcuts import HttpResponse


# def index(request):
#     return HttpResponse('index')
#
# def topics(request):
#     return HttpResponse('topics')


def index(request):
    ''' Mane page'''
    return render(request, 'notebook/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def topics(request):
#     ''' topics list page'''
#     topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notebook/topics.html', context)