from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
# модуль для хранения текущих представлений(то что мы будем видеть)

# Create your views here.

def index(request):
    res = request.GET
    print(request.GET)
    return HttpResponse(f'Главная страница основного приложения<br> {dict(res)}')

def categorys(request):
    return HttpResponse('<h1> ссылки по категориям </h1>')

def category(request, cat_id):
    if cat_id >1000:
        raise Http404()
    return HttpResponse(f'<h1> Номер категории - </h1> <br> {cat_id}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')