# Generated by Django 5.0.4 on 2024-08-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessuar', '0007_accessuardownloadfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikulAccessuar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikul', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]