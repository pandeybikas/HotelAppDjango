# Generated by Django 4.2.1 on 2023-05-07 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.hotel'),
        ),
    ]