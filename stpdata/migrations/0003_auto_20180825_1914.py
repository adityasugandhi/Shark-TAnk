# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-25 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stpdata', '0002_auto_20180825_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='corcoran',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cuban',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deal',
        ),
        migrations.RemoveField(
            model_name='product',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='product',
            name='equity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='greiner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='guests',
        ),
        migrations.RemoveField(
            model_name='product',
            name='harrington',
        ),
        migrations.RemoveField(
            model_name='product',
            name='herjavec',
        ),
        migrations.RemoveField(
            model_name='product',
            name='investPer_shark',
        ),
        migrations.RemoveField(
            model_name='product',
            name='john',
        ),
        migrations.RemoveField(
            model_name='product',
            name='no_of_sharks',
        ),
        migrations.RemoveField(
            model_name='product',
            name='note',
        ),
        migrations.RemoveField(
            model_name='product',
            name='olary',
        ),
        migrations.RemoveField(
            model_name='product',
            name='season',
        ),
        migrations.RemoveField(
            model_name='product',
            name='valuation',
        ),
    ]
