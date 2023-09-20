from django.http import HttpResponse
from django.shortcuts import render
# модуль для хранения текущих представлений(то что мы будем видеть)

# Create your views here.

def index(request):
    return HttpResponse('Главная страница основного приложения')

def categorys(request):
    return HttpResponse('<h1> ссылки по категориям </h1>')

def category(request, cat_id):
    return HttpResponse(f'<h1> Номер категории - </h1> <br> {cat_id}')