# Generated by Django 4.2.1 on 2023-05-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_menu_hotel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='menuItem',
            field=models.ManyToManyField(to='home.menu'),
        ),
    ]
