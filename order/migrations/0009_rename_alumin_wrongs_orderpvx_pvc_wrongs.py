# Generated by Django 3.2.20 on 2023-09-26 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_orderpvx_order_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpvx',
            old_name='alumin_wrongs',
            new_name='pvc_wrongs',
        ),
    ]