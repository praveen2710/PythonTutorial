# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
