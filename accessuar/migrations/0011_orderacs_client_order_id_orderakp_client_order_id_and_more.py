# Generated by Django 5.0.4 on 2024-08-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessuar', '0010_orderakp_order_name_orderprochiye_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderacs',
            name='client_order_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orderakp',
            name='client_order_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orderprochiye',
            name='client_order_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]