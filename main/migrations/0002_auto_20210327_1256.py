# Generated by Django 3.0 on 2021-03-27 07:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
