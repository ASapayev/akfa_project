# Generated by Django 5.0.4 on 2024-07-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiator', '0007_alter_radiatorsapcode_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikulRadiator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikul', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
