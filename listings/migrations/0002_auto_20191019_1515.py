# Generated by Django 2.2.5 on 2019-10-19 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2019, 10, 19, 15, 15, 25, 612564)),
        ),
    ]
