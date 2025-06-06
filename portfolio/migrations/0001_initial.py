# Generated by Django 5.1.6 on 2025-02-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='project_images/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
