# Generated by Django 4.2 on 2023-04-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreArtist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('short_biography', models.TextField(max_length=500)),
                ('description_artist', models.TextField()),
                ('genres', models.ManyToManyField(related_name='genres_artist', to='artists.genreartist')),
            ],
        ),
    ]