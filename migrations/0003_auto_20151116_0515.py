# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20151112_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stripeorder',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='stripeorder',
            name='site',
        ),
        migrations.DeleteModel(
            name='StripeOrder',
        ),
    ]
