# Generated by Django 4.1.1 on 2022-11-17 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('actorid', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('directorid', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movieid', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('language', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
            ],
        ),
    ]
