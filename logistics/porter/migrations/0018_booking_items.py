# Generated by Django 3.1.2 on 2021-03-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porter', '0017_auto_20210327_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='items',
            field=models.CharField(default='Boxes', max_length=500),
        ),
    ]