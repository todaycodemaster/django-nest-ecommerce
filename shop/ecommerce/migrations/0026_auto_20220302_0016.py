# Generated by Django 3.2 on 2022-03-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0025_auto_20220302_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pallet_units',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pallet_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]