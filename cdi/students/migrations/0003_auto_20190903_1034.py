# Generated by Django 2.2.4 on 2019-09-03 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190902_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 9, 3, 10, 34, 52, 754661), help_text='Año-Mes-Dia', null=True),
        ),
    ]
