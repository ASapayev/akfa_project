# Generated by Django 5.0.4 on 2024-10-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesavdo', '0007_remove_buxprice_data_remove_segment_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='segment_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
