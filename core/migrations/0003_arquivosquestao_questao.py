# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171104_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivosQuestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'ArquivosQuestao',
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('data_limite_entrega', models.DateField()),
                ('numero', models.IntegerField()),
                ('data', models.DateField()),
            ],
            options={
                'db_table': 'Questao',
            },
        ),
    ]
