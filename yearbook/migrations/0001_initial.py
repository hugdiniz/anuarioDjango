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
                ('comentarios', models.CharField(max_length=500, blank=True)),
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
                ('cargo', models.ForeignKey(to='yearbook.Cargo')),
                ('historico', models.ManyToManyField(related_name=b'lotacoes_anteriores', to='yearbook.Lotacao', blank=True)),
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
                ('predio', models.CharField(max_length=200)),
                ('andar', models.IntegerField()),
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
                ('sigla', models.CharField(max_length=200, blank=True)),
                ('telefone', models.CharField(max_length=30)),
                ('ramal', models.CharField(max_length=5)),
                ('localidade', models.CharField(max_length=300)),
                ('parent', models.ForeignKey(related_name=b'children', to='yearbook.Unidade_Organizacional', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sala',
            name='uorg',
            field=models.ForeignKey(to='yearbook.Unidade_Organizacional'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lotacao',
            name='sala',
            field=models.ForeignKey(to='yearbook.Sala', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lotacao',
            name='uorg',
            field=models.ForeignKey(to='yearbook.Unidade_Organizacional'),
            preserve_default=True,
        ),
    ]
