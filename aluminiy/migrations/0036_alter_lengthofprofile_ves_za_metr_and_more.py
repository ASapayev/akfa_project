# Generated by Django 5.0.4 on 2024-10-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0035_alter_lengthofprofile_ves_za_metr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lengthofprofile',
            name='ves_za_metr',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='lengthofprofile',
            name='ves_za_shtuk',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
