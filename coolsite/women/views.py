from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseForbidden, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect


# модуль для хранения текущих представлений(то что мы будем видеть)

# Create your views here.
menu =['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            }
    return render(request, 'women/index.html', data)

def categorys(request):
    return HttpResponse('<h1> ссылки по категориям </h1>')

def category(request, cat_id):
    if cat_id >1000:
        raise Http404()
    if cat_id < 50:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> Номер категории - </h1> <br> {cat_id}')

def year_archive(request, year):

    return HttpResponse(f'<h1> Год какой-то -  </h1> <br> {year}')

def alphabet(request, alt):

    return HttpResponse(f'<h1> Маршрут -  </h1> <br> {alt}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')

