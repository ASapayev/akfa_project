# Generated by Django 4.0 on 2024-03-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvc', '0029_nakleykapvc'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikulkomponentpvc',
            name='iskyucheniye',
            field=models.CharField(blank=True, default='0', max_length=5, null=True),
        ),
    ]