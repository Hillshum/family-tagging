# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ancestor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('given_names', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('photo', models.FileField(upload_to='')),
                ('caption', models.CharField(max_length=150)),
                ('taken_date', models.DateTimeField(verbose_name='date taken')),
            ],
        ),
        migrations.CreateModel(
            name='PictureRelationship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ancestor', models.ForeignKey(to='family_tags.Ancestor')),
                ('photo', models.ForeignKey(to='family_tags.Photo')),
            ],
        ),
        migrations.AddField(
            model_name='ancestor',
            name='photos',
            field=models.ManyToManyField(through='family_tags.PictureRelationship', to='family_tags.Photo'),
        ),
    ]
