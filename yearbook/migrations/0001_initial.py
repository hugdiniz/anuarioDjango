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
                ('data_inicio', models.DateField(verbose_name=b'data_inicio')),
                ('data_saida', models.DateField(verbose_name=b'data_saida')),
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
                ('entrada', models.DateField(auto_now_add=True, verbose_name=b'data de entrada', null=True)),
                ('afastamento', models.DateField(null=True, verbose_name=b'data de afastamento', blank=True)),
                ('funcao', models.ForeignKey(blank=True, to='yearbook.Funcao', null=True)),
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
                ('telefone', models.CharField(max_length=30)),
                ('ramal', models.CharField(max_length=5)),
                ('nascimento', models.DateField(verbose_name=b'data de nascimento')),
                ('foto', models.CharField(max_length=200, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('ferias_inicio', models.DateField(null=True, verbose_name=b'inicio das ferias', blank=True)),
                ('ferias_fim', models.DateField(null=True, verbose_name=b'fim das ferias', blank=True)),
                ('licenca_inicio', models.DateField(null=True, verbose_name=b'inicio licenca', blank=True)),
                ('licenca_fim', models.DateField(null=True, verbose_name=b'fim licenca', blank=True)),
                ('cargo', models.ForeignKey(to='yearbook.Cargo')),
                ('historico', models.ManyToManyField(related_name=b'lotacoes_anteriores', to='yearbook.Lotacao', blank=True)),
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
                ('localidade', models.CharField(max_length=300, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('localidade_sala', models.ForeignKey(blank=True, to='yearbook.Sala', null=True)),
                ('parent', models.ForeignKey(related_name=b'children', blank=True, to='yearbook.Unidade_Organizacional', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=16)),
                ('uorg', models.ForeignKey(to='yearbook.Unidade_Organizacional')),
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
            name='pessoa',
            field=models.ForeignKey(to='yearbook.Pessoa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lotacao',
            name='sala',
            field=models.ForeignKey(blank=True, to='yearbook.Sala', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lotacao',
            name='uorg',
            field=models.ForeignKey(to='yearbook.Unidade_Organizacional'),
            preserve_default=True,
        ),
    ]
