# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0004_auto_20141212_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lotacao',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='historico',
            field=models.ManyToManyField(related_name=b'lotacoes_anteriores', to='yearbook.Lotacao', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unidade_organizacional',
            name='localidade_sala',
            field=models.ForeignKey(blank=True, to='yearbook.Sala', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lotacao',
            name='funcao',
            field=models.ForeignKey(blank=True, to='yearbook.Funcao', null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ferias_fim',
            field=models.DateTimeField(null=True, verbose_name=b'fim das ferias', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ferias_inicio',
            field=models.DateTimeField(null=True, verbose_name=b'inicio das ferias', blank=True),
        ),
    ]
