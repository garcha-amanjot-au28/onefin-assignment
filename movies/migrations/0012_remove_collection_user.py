# Generated by Django 4.1 on 2022-08-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_collection_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
    ]