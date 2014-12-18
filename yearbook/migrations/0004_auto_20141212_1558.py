# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0003_auto_20141212_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='historico',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='lotacao_atual',
        ),
        migrations.AddField(
            model_name='lotacao',
            name='pessoa',
            field=models.ForeignKey(default='1', to='yearbook.Pessoa'),
            preserve_default=False,
        ),
    ]
