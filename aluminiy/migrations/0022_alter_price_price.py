# Generated by Django 4.2.1 on 2023-08-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0021_lengthofprofile_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(),
        ),
    ]
