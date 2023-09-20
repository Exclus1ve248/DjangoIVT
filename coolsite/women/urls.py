from django.urls import path

from women.views import *

urlpatterns = [
    path('', index),
    path('cat/', categorys),
    path('cat/<int:cat_id>/', category),
]