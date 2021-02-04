# Generated by Django 3.1.6 on 2021-02-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_episode'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('animes', models.ManyToManyField(to='main_app.Anime')),
                ('episodes', models.ManyToManyField(to='main_app.Episode')),
            ],
        ),
    ]
