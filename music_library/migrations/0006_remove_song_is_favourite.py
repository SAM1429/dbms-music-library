# Generated by Django 4.1.4 on 2023-01-05 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0005_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favourite',
        ),
    ]
