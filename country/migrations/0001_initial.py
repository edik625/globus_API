# Generated by Django 5.0.6 on 2024-06-08 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descripten', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('descripten', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capital', models.CharField(max_length=30)),
                ('population', models.BigIntegerField()),
                ('area', models.FloatField()),
                ('language', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=30)),
                ('climat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.climat')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.continent')),
            ],
        ),
    ]