# Generated by Django 4.2.2 on 2024-01-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("song", "0002_rename_title_artist_name_song_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="lyric",
            field=models.TextField(blank=True, null=True),
        ),
    ]