# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0004_auto_20141209_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade_organizacional',
            name='localidade',
            field=models.CharField(default='none', max_length=300),
            preserve_default=False,
        ),
    ]
