# Generated by Django 3.2.20 on 2023-12-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normabenkam', '0008_nakleyka'),
    ]

    operations = [
        migrations.AddField(
            model_name='ximikat',
            name='alufinish',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ximikat',
            name='chemetal7400',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ximikat',
            name='chemetal7406',
            field=models.SmallIntegerField(default=0),
        ),
    ]
