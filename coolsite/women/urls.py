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

class FourDigitAlpConv:
    regex = '[A-z]'
    def to_python(self, alt):
        return str(alt)

    def to_url(selfself, value):
        return 0

register_converter(FourDigitAlpConv, 'a')

urlpatterns = [
    path('', index, name='home'),
    path('cat/', categorys),
    path('art/<a:alt>/', alphabet),
    path("articles/<yyyy:year>/", year_archive),
    path('cat/<int:cat_id>/', category),
    path('get/', post_detail)
]