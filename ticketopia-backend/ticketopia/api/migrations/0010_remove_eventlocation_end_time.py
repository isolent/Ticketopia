# Generated by Django 3.2 on 2023-05-03 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20230502_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlocation',
            name='end_time',
        ),
    ]
