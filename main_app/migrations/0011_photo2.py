# Generated by Django 3.1.6 on 2021-02-08 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210207_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.episode')),
            ],
        ),
    ]
