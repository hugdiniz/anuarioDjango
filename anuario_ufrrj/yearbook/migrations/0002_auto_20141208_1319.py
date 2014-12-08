# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='andar',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sala',
            name='predio',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
