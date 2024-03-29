# Generated by Django 5.0.2 on 2024-02-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songThumbnail', models.ImageField(help_text='.jpg, .png, .jpeg, .gif, .svg supported', upload_to='thumbnail/', verbose_name='Song Thumbnail')),
                ('song', models.FileField(help_text='.mp3 supported only', upload_to='songs/', verbose_name='Song')),
                ('songName', models.CharField(max_length=50, verbose_name='Song Name')),
                ('genre', models.CharField(choices=[('C', 'Classical'), ('HH', 'Hip-Hop'), ('J', 'Jazz'), ('F', 'Funck'), ('R', 'R-N-B'), ('P', 'Pop'), ('RK', 'Rock'), ('M', 'Metal')], max_length=2)),
                ('artist_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Song created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest song update')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
    ]
