# Generated by Django 3.2.18 on 2023-04-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiytermo', '0008_alufiletermo_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='NakleykaCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
