# Generated by Django 4.1 on 2022-08-09 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_movie_movie_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='collection',
        ),
        migrations.AddField(
            model_name='movie',
            name='collection',
            field=models.ManyToManyField(related_name='movies', to='movies.collection'),
        ),
    ]
