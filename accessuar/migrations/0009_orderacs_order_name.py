# Generated by Django 5.0.4 on 2024-08-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessuar', '0008_artikulaccessuar'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderacs',
            name='order_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
