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
    slug = models.SlugField(max_length=255, db_index=True, unique=True)


    def get_absolute_url(self):
        return reverse('group', kwargs={'group_slug':self.slug})


class Books(models.Model):
    name = models.CharField(max_length=60)
    cost = models.IntegerField()



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



