# Generated by Django 4.2.1 on 2023-08-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0022_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lengthofprofile',
            name='length',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='lengthofprofile',
            name='ves_za_metr',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='lengthofprofile',
            name='ves_za_shtuk',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.CharField(max_length=150),
        ),
    ]
