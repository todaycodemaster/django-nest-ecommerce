# Generated by Django 3.2 on 2022-02-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_shipping_regions'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='vat_french',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
