from django.urls import path, register_converter

from women.views import *

from women.views import category, index, categorys


class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(selfself, value):
        return "%04d" % value


register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', index, name='home'),
    path('cat/', categorys),
    path("articles/<yyyy:year>/", year_archive),
    path('cat/<int:cat_id>/', category),
]