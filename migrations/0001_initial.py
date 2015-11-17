# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150527_1127'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True, blank=True)),
                ('stripe_id', models.IntegerField(null=True, blank=True)),
                ('currency', models.CharField(max_length=4, verbose_name='First name')),
                ('paid', models.BooleanField()),
                ('order_id', models.ForeignKey(to='shop.Order')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
