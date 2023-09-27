from django.urls import path

from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('cat/', categorys),
    path('cat/<int:cat_id>/', category),
]