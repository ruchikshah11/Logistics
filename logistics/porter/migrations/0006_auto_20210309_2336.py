# Generated by Django 3.1.2 on 2021-03-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porter', '0005_auto_20210309_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]