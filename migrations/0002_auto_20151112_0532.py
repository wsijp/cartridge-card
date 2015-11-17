# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripeorder',
            name='currency',
            field=models.CharField(max_length=4, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='stripeorder',
            name='stripe_id',
            field=models.CharField(default=0, max_length=100, verbose_name='Stripe ID'),
            preserve_default=False,
        ),
    ]
