# Generated by Django 3.1.6 on 2021-02-07 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='article',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='episode',
        ),
    ]