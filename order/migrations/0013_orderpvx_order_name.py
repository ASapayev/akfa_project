# Generated by Django 5.0.4 on 2024-08-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_order_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpvx',
            name='order_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]