# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-14 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180414_1922'),
        ('courses', '0002_auto_20180407_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cours_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='课程机构'),
        ),
    ]
