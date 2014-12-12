# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0007_auto_20141211_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lotacao',
            name='nome',
        ),
        migrations.AddField(
            model_name='lotacao',
            name='comentarios',
            field=models.CharField(default='empty', max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lotacao',
            name='uorg',
            field=models.ForeignKey(default=0, to='yearbook.Unidade_Organizacional'),
            preserve_default=False,
        ),
    ]
