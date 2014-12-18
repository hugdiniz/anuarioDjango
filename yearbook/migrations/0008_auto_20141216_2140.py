# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0007_auto_20141216_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotacao',
            name='afastamento',
            field=models.DateField(null=True, verbose_name=b'data de afastamento', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='licenca_fim',
            field=models.DateField(null=True, verbose_name=b'fim licenca', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='licenca_inicio',
            field=models.DateField(null=True, verbose_name=b'inicio licenca', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lotacao',
            name='sala',
            field=models.ForeignKey(blank=True, to='yearbook.Sala', null=True),
        ),
    ]
