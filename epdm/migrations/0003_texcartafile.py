# Generated by Django 5.0.4 on 2024-09-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epdm', '0002_rename_norma75_normaepdm'),
    ]

    operations = [
        migrations.CreateModel(
            name='TexcartaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=500, upload_to='uploads/epdm/downloads/')),
                ('generated', models.BooleanField(default=False)),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]