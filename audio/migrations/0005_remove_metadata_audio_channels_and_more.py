# Generated by Django 4.2.6 on 2023-10-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_alter_metadata_album_alter_metadata_artist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='audio_channels',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='custom_metadata',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='musical_genre',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='sample_rate',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='year_recorded',
        ),
        migrations.AlterField(
            model_name='metadata',
            name='album',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='artist',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='authors',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='track_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='where_from',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]