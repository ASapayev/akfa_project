# Generated by Django 4.2.1 on 2023-05-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_excelfiles_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sena_za_metr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sena_za_shtuk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ves_del_odxod',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
