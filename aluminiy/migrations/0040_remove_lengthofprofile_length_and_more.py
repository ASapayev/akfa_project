# Generated by Django 5.0.4 on 2024-10-29 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0039_lengthofprofile_component_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lengthofprofile',
            name='length',
        ),
        migrations.RemoveField(
            model_name='lengthofprofile',
            name='ves_za_shtuk',
        ),
    ]
