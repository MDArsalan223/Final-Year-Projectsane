# Generated by Django 5.0.2 on 2024-02-16 07:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('tagline', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NS', 'Rather not to say')], max_length=2)),
                ('Nationality', models.TextField(blank=True)),
                ('Address', models.TextField(blank=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
