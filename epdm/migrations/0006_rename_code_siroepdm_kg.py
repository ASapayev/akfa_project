# Generated by Django 5.0.4 on 2024-09-17 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epdm', '0005_siroepdm_shop_alter_siroepdm_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siroepdm',
            old_name='code',
            new_name='kg',
        ),
    ]
