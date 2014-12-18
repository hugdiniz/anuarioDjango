# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0005_auto_20141214_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotacao',
            name='entrada',
            field=models.DateField(auto_now_add=True, verbose_name=b'data de entrada', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ramal',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unidade_organizacional',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ferias_fim',
            field=models.DateField(null=True, verbose_name=b'fim das ferias', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ferias_inicio',
            field=models.DateField(null=True, verbose_name=b'inicio das ferias', blank=True),
        ),
    ]
