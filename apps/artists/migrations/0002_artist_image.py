# Generated by Django 4.2 on 2023-04-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(default=1, upload_to='Photo/Artists/'),
            preserve_default=False,
        ),
    ]