# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0008_auto_20141216_2140'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(verbose_name=b'data de nascimento'),
        ),
        migrations.AlterField(
            model_name='unidade_organizacional',
            name='parent',
            field=models.ForeignKey(related_name=b'children', blank=True, to='yearbook.Unidade_Organizacional', null=True),
        ),
    ]
