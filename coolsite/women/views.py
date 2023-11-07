from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseForbidden, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect


# модуль для хранения текущих представлений(то что мы будем видеть)

# Create your views here.
menu =[{'title': 'Главная', 'url': 'home'},
       {'title': 'О сайте', 'url': 'about'},
       {'title': 'Красивый css', 'url': 'cub'}
       ]



def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,

            }
    return render(request, 'women/index.html', context=data)

def about(request):
    data = {'title': 'О программе',
            'menu': menu,
            }
    return render(request, 'women/index.html', context=data)

def cub(request):
    data = {'title': 'О программе',
            'menu': menu,
            }
    return render(request, 'women/3D_kub.html', context=data)

def categorys(request):
    return HttpResponse('<h1> ссылки по категориям </h1>')

def category(request, cat_id):
    if cat_id >1000:
        raise Http404()
    if cat_id < 0:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> Номер категории - </h1> <br> {cat_id}')




def year_archive(request, year):

    return HttpResponse(f'<h1> Год какой-то -  </h1> <br> {year}')

def alphabet(request, alt):

    return HttpResponse(f'<h1> Маршрут -  </h1> <br> {alt}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')

def post_detail(request):
    if(request.GET):
        converted = str()
        for key in request.GET:
            converted += key + '= ' + request.GET[key] + '|'
        return HttpResponse(f'<p>{converted[:-1]}</p>')
    return HttpResponse('<p>GET is empty</p>')

