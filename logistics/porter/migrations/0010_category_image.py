# Generated by Django 3.1.2 on 2021-03-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porter', '0009_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
