# Generated by Django 3.2.20 on 2023-08-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0010_vifiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='norma',
            name='ala7_oddiy_ala8_qora_алю_сплав_6064_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='norma',
            name='алю_сплав_биллетов_102_178_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
