# Generated by Django 5.0.4 on 2024-10-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluminiy', '0038_alter_lengthofprofile_ves_za_metr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lengthofprofile',
            name='component',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lengthofprofile',
            name='artikul',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]