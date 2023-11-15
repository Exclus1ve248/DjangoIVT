import datetime

from django.db import models
# для хранения ORM-моделей для представления данных из базы данных

# Create your models here

dt_now = datetime.datetime.now()

class Students(models.Model):
    fio = models.CharField(max_length=30)
    interesting = models.TextField(blank=True)
    birthday = models.DateTimeField(default=dt_now)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_money = models.BooleanField(default=True)

    def __str__(self):
        return self.fio

"""
создание записей
 Students.objects.create(fio="Ковалев Егор Павлович", interesting="программирование")
выбор всех записей
Students.objects.all()
выбор записей по критериям
Students.objects.filter(pk=2)
изменение всех записей
Students.objects.update(is_profoom=0)
удаление записи
wd.delete()
"""


class Books(models.Model):
    name = models.CharField(max_length=40)
    cost = models.IntegerField()
