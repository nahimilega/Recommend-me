# Generated by Django 2.1.5 on 2019-02-12 13:50

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20190207_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='rest_all_the_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_feature_matrix', djongo.models.fields.DictField()),
                ('movie_feature_matrix', djongo.models.fields.DictField()),
                ('top_movies', djongo.models.fields.ListField()),
                ('movie_movie_matrix', djongo.models.fields.DictField()),
            ],
        ),
    ]
