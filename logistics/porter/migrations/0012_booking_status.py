# Generated by Django 3.1.2 on 2021-03-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porter', '0011_booking_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
