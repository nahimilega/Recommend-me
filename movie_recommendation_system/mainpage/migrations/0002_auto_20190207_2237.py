# Generated by Django 2.1.5 on 2019-02-07 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='updated_at',
        ),
    ]