# Generated by Django 4.0 on 2023-12-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlyuminniysilindrEkstruziya1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_code_s4q100', models.CharField(blank=True, max_length=255, null=True)),
                ('название', models.CharField(blank=True, max_length=255, null=True)),
                ('еи', models.CharField(blank=True, max_length=255, null=True)),
                ('склад_закупа', models.CharField(blank=True, max_length=255, null=True)),
                ('тип', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
