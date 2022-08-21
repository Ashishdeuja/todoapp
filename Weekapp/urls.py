from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.index, name ='index'),
    path('page1/',views.page1, name ='page1'),
    path('question/',views.question, name ='question'),
    path('myform/', views.question_form, name='form'),
    path('',views.todo,name='todoform')
]