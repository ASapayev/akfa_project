# Generated by Django 5.0.4 on 2024-08-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessuar', '0006_orderakp_orderprochiye'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessuarDownloadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=500, upload_to='uploads/accessuar/downloads/')),
                ('generated', models.BooleanField(default=False)),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
