# Generated by Django 3.2.20 on 2023-12-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normabenkam', '0005_norma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_code_s4q100', models.CharField(blank=True, max_length=255, null=True)),
                ('название', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
