# Generated by Django 5.0.4 on 2024-10-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesavdo', '0006_buxprice_segment_zavod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buxprice',
            name='data',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='data',
        ),
        migrations.RemoveField(
            model_name='zavod',
            name='data',
        ),
        migrations.AddField(
            model_name='buxprice',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='buxprice',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='zavod',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='zavod',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
