# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('nascimento', models.DateTimeField(verbose_name=b'data de nascimento')),
                ('foto', models.CharField(max_length=200, blank=True)),
                ('historico', models.ManyToManyField(related_name=b'lotacoes_anteriores', to='yearbook.Lotacao')),
                ('lotacao_atual', models.ForeignKey(to='yearbook.Lotacao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificador', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unidade_Organizacional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('abreviacao', models.CharField(max_length=200, blank=True)),
                ('parent', models.ForeignKey(related_name=b'children', to='yearbook.Unidade_Organizacional', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sala',
            name='unidade',
            field=models.ForeignKey(to='yearbook.Unidade_Organizacional'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='oucupante',
            field=models.ForeignKey(to='yearbook.Pessoa'),
            preserve_default=True,
        ),
    ]
