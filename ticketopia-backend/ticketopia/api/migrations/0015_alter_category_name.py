# Generated by Django 3.2 on 2023-05-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20230503_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Movie', 'Movies'), ('Concerts', 'Concerts'), ('Theatre', 'Theatre')], max_length=255, unique=True),
        ),
    ]