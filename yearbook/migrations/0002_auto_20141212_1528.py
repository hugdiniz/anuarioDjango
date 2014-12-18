# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade_organizacional',
            name='localidade',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
