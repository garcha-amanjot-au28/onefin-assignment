# Generated by Django 4.1 on 2022-08-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
