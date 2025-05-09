# Generated by Django 5.1.7 on 2025-03-19 20:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.EmailField(blank=True, max_length=250)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
