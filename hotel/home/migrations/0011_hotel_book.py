# Generated by Django 4.2.1 on 2023-05-08 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_booking_hotel'),
        ('home', '0010_hotel_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='booking.booking'),
        ),
    ]
