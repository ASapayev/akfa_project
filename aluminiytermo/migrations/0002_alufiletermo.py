# Generated by Django 3.2.18 on 2023-03-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiytermo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AluFileTermo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('generated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
