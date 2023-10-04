from django.urls import path

from women.views import *

from women.views import category, index, categorys

urlpatterns = [
    path('', index, name='home'),
    path('cat/', categorys),
    path('cat/<int:cat_id>/', category),
]