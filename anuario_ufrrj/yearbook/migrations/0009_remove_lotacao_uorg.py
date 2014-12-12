# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0008_auto_20141212_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lotacao',
            name='uorg',
        ),
    ]
