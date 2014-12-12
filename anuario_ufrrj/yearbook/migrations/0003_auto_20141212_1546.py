# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0002_auto_20141212_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='ferias_fim',
            field=models.DateTimeField(default=datetime.date(2014, 12, 12), verbose_name=b'ferias_fim', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ferias_inicio',
            field=models.DateTimeField(default=datetime.date(2014, 12, 12), verbose_name=b'ferias_inicio', blank=True),
            preserve_default=False,
        ),
    ]
