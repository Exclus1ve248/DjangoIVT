# Generated by Django 4.2.6 on 2023-11-22 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_students_slug_alter_students_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 22, 9, 0, 4, 87066)),
        ),
    ]
