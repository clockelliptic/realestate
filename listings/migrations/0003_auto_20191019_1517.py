# Generated by Django 2.2.5 on 2019-10-19 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191019_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='Pennsylvania', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2019, 10, 19, 15, 17, 3, 244357)),
        ),
    ]