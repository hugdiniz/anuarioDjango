# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0006_auto_20141214_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcao',
            name='data_inicio',
            field=models.DateField(default=datetime.date(2014, 12, 16), verbose_name=b'data_inicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcao',
            name='data_saida',
            field=models.DateField(default=datetime.date(2014, 12, 16), verbose_name=b'data_saida'),
            preserve_default=False,
        ),
    ]
