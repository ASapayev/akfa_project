# Generated by Django 4.2.1 on 2023-07-26 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0009_zakalkaiskyuchenie'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=500, upload_to='uploads/vi/downloads')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]