from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # ex: /topics/5/
    path('<int:question_id>/', index, name='topics'),

]