# Generated by Django 4.0 on 2024-03-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
