# Generated by Django 3.2 on 2022-02-18 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_remove_dataprotection_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataprotection',
            old_name='legal_advise',
            new_name='legal_advice',
        ),
    ]