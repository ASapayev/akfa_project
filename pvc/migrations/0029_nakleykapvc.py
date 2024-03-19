# Generated by Django 4.0 on 2024-03-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvc', '0028_artikulkomponentpvc_kod_k_component'),
    ]

    operations = [
        migrations.CreateModel(
            name='NakleykaPvc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('nadpis', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]