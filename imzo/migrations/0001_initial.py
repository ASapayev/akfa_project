# Generated by Django 3.2.18 on 2023-05-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFilesImzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=500, upload_to='uploads/imzo/downloads')),
                ('generated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImzoBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=255)),
                ('kratkiytekst', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TexCartaTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('компонент_1', models.CharField(blank=True, max_length=255, null=True)),
                ('компонент_2', models.CharField(blank=True, max_length=255, null=True)),
                ('компонент_3', models.CharField(blank=True, max_length=255, null=True)),
                ('артикул', models.CharField(blank=True, max_length=255, null=True)),
                ('пресс_1_линия_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('закалка_1_печь_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('покраска_SKM_белый_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('покраска_SAT_базовый_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('покраска_горизонтал_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('покраска_ручная_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('вакуум_1_печка_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('термо_1_линия_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('наклейка_упаковка_1_линия_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('ламинат_1_линия_про_во_в_сутки_буй', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
