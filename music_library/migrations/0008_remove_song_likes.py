# Generated by Django 4.1.4 on 2023-01-05 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0007_song_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='likes',
        ),
    ]
