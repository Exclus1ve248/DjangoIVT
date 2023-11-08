from django.db import models
# для хранения ORM-моделей для представления данных из базы данных

# Create your models here

class Students(models.Model):
    fio = models.CharField(max_length=30)
    interesting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_money = models.BooleanField(default=True)
