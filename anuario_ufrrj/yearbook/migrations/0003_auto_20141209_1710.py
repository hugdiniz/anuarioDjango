# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0002_auto_20141208_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade_organizacional',
            name='ramal',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unidade_organizacional',
            name='telefone',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
