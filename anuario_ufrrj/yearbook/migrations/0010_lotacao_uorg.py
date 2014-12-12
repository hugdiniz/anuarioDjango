# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0009_remove_lotacao_uorg'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotacao',
            name='uorg',
            field=models.ForeignKey(default=1, to='yearbook.Unidade_Organizacional'),
            preserve_default=False,
        ),
    ]
