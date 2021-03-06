# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-31 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('email', models.CharField(max_length=255, null=True)),
                ('exam_1', models.BooleanField(default=True)),
                ('exam_2', models.BooleanField(default=True)),
                ('exam_3', models.BooleanField(default=True)),
                ('age', models.IntegerField()),
                ('url_img', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_topic', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='singleproject.Coder')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=90)),
                ('date', models.DateField(max_length=8, null=True)),
                ('password', models.CharField(max_length=355)),
                ('admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='singleproject.User'),
        ),
    ]
