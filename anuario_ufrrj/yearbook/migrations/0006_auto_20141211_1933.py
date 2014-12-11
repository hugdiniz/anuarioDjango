# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0005_unidade_organizacional_localidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='historico',
            field=models.ManyToManyField(related_name=b'lotacoes_anteriores', to=b'yearbook.Lotacao', blank=True),
        ),
    ]
