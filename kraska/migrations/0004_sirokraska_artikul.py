# Generated by Django 5.0.4 on 2024-10-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kraska', '0003_sirokraska_texcartafile'),
    ]

    operations = [
        migrations.AddField(
            model_name='sirokraska',
            name='artikul',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
