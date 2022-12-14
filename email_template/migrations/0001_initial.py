# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-22 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('to_email', models.CharField(blank=True, max_length=255, null=True)),
                ('from_email', models.CharField(blank=True, max_length=255, null=True)),
                ('html_template', models.TextField(blank=True, null=True)),
                ('plain_text', models.TextField(blank=True, null=True)),
                ('is_html', models.BooleanField(default=False)),
                ('is_text', models.BooleanField(default=False)),
                ('template_key', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
