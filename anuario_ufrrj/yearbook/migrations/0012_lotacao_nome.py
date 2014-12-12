# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0011_auto_20141212_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotacao',
            name='nome',
            field=models.CharField(default='Sem nome', max_length=100),
            preserve_default=False,
        ),
    ]
