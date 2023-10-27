# Generated by Django 3.2.20 on 2023-10-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvc', '0019_auto_20231020_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='DliniyText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_code', models.CharField(blank=True, max_length=150, null=True)),
                ('product_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
