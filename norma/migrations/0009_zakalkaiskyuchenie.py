# Generated by Django 4.2.1 on 2023-07-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0008_normaexcelfiles_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZakalkaIskyuchenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_code', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
