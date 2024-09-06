# Generated by Django 5.0.4 on 2024-07-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0032_mastergroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuxgalterNazvaniye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colected', models.CharField(blank=True, max_length=40, null=True)),
                ('combination', models.CharField(blank=True, max_length=40, null=True)),
                ('surface_treatment', models.CharField(blank=True, max_length=40, null=True)),
                ('zavod_aluminiy', models.CharField(blank=True, max_length=80, null=True)),
                ('zavod_aluminiy_benkam', models.CharField(blank=True, max_length=80, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
