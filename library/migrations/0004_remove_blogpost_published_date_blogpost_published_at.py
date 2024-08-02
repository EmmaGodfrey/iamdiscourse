# Generated by Django 5.0.4 on 2024-08-02 13:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_resource_file_resource_resource_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='published_date',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
