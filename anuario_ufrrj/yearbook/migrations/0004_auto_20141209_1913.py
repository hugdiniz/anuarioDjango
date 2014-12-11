# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0003_auto_20141209_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unidade_organizacional',
            old_name='abreviacao',
            new_name='sigla',
        ),
    ]
