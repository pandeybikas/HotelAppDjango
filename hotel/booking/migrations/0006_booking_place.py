# Generated by Django 4.2.1 on 2023-05-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_booking_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='place',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
