# Generated by Django 2.2.4 on 2019-09-12 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20190906_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 9, 12, 16, 30, 4, 600157), help_text='Año-Mes-Dia', null=True),
        ),
    ]
