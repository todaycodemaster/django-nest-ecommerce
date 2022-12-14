# Generated by Django 3.2 on 2022-02-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_rename_legal_advise_dataprotection_legal_advice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataprotection',
            name='cookies_web',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='dataprotection',
            name='display_text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='dataprotection',
            name='legal_advice',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='dataprotection',
            name='privacy_policy',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
