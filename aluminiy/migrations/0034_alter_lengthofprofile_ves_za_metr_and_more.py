# Generated by Django 5.0.4 on 2024-10-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0033_buxgalternazvaniye'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lengthofprofile',
            name='ves_za_metr',
            field=models.JSONField(default={'Анодированный': '', 'Белый': '', 'Ламинированный': '', 'Неокрашенный': '', 'Окрашенный': '', 'Сублимированный': ''}),
        ),
        migrations.AlterField(
            model_name='lengthofprofile',
            name='ves_za_shtuk',
            field=models.JSONField(default={'Анодированный': '', 'Белый': '', 'Ламинированный': '', 'Неокрашенный': '', 'Окрашенный': '', 'Сублимированный': ''}),
        ),
    ]
