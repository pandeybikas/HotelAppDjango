# Generated by Django 4.2.1 on 2023-05-08 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_hotel_menu_hotel_name_rename_image_menu_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='hotel_name',
        ),
    ]
