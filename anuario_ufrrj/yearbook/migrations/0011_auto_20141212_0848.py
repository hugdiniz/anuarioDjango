# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0010_lotacao_uorg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sala',
            old_name='unidade',
            new_name='uorg',
        ),
    ]
