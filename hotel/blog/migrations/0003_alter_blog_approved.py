# Generated by Django 4.2.1 on 2023-05-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_tag_delete_tag_blog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='approved',
            field=models.BooleanField(null=True),
        ),
    ]
