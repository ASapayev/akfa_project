# Generated by Django 3.2.20 on 2023-08-30 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0012_zakalkaiskyuchenie6064'),
    ]

    operations = [
        migrations.RenameField(
            model_name='norma',
            old_name='ala7_oddiy_ala8_qora_алю_сплав_6064',
            new_name='qora_алю_сплав_6064_sap_code',
        ),
        migrations.RemoveField(
            model_name='norma',
            name='ala7_oddiy_ala8_qora_алю_сплав_6064_2',
        ),
        migrations.RemoveField(
            model_name='norma',
            name='алю_сплав_биллетов_102_178',
        ),
        migrations.RemoveField(
            model_name='norma',
            name='алю_сплав_биллетов_102_178_2',
        ),
    ]
