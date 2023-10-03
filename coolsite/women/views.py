from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseForbidden, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect


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
    if cat_id < 50:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> Номер категории - </h1> <br> {cat_id}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')

def serverError(request, template_name='500.html'):

    return HttpResponseServerError(f'<h1> ошибка </h1>')
def Forbidden(request, exception, template_name='403.html'):
    return HttpResponseForbidden('')

def badRequest(request, exception, template_name='400.html'):
    return HttpResponseBadRequest('')