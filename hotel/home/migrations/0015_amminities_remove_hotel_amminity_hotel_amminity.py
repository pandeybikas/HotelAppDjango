# Generated by Django 4.2.1 on 2023-05-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_hotel_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amminities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('icon', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='amminity',
        ),
        migrations.AddField(
            model_name='hotel',
            name='amminity',
            field=models.ManyToManyField(to='home.amminities'),
        ),
    ]