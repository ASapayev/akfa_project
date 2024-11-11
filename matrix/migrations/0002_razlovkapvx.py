# Generated by Django 5.0.4 on 2024-11-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RazlovkaPVX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('nkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('tchsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('tchkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('fchsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('fchkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('zsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('zkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('shsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('shkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('tsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('tkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('fsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('fkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('edmsapkode', models.CharField(blank=True, max_length=50, null=True)),
                ('edmkrat', models.CharField(blank=True, max_length=50, null=True)),
                ('sapkode7', models.CharField(blank=True, max_length=50, null=True)),
                ('krat7', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
