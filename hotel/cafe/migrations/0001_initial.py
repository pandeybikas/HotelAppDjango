# Generated by Django 4.2.1 on 2023-05-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_name', models.CharField(max_length=100, null=True)),
                ('cafe_image', models.ImageField(null=True, upload_to='media')),
                ('address', models.TextField(null=True)),
                ('about', models.TextField(null=True)),
                ('speciality', models.CharField(choices=[('', 'Choose feature'), ('Ambient', 'Ambient'), ('Food', 'Food'), ('Location', 'Location'), ('Hospitality', 'Hospitality')], max_length=100, null=True)),
                ('feeder_name', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
