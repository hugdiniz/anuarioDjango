# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('funcao', models.ForeignKey(to='yearbook.Funcao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cargo',
            name='oucupante',
            field=models.ForeignKey(default=None, to='yearbook.Pessoa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='historico',
            field=models.ManyToManyField(related_name=b'lotacoes_anteriores', to='yearbook.Lotacao'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='lotacao_atual',
            field=models.ForeignKey(default=None, to='yearbook.Lotacao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sala',
            name='unidade',
            field=models.ForeignKey(default=None, to='yearbook.Unidade_Organizacional'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unidade_organizacional',
            name='unidade_org',
            field=models.ForeignKey(default=None, to='yearbook.Unidade_Organizacional'),
            preserve_default=False,
        ),
    ]
