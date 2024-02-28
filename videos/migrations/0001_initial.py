# Generated by Django 5.0.2 on 2024-02-28 07:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('description', ckeditor.fields.RichTextField()),
                ('file', models.FileField(upload_to='video_files_uploads/')),
                ('is_active', models.BooleanField(default=True)),
                ('tags', models.ManyToManyField(to='videos.tag')),
            ],
        ),
    ]