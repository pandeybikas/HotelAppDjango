# Generated by Django 4.2.1 on 2023-05-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_hotel_menuitem_menu_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
