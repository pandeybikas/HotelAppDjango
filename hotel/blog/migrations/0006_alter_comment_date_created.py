# Generated by Django 4.2.1 on 2023-05-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
