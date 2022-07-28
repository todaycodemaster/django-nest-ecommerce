# Generated by Django 3.2 on 2022-03-04 12:21

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0030_auto_20220304_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_thumbnail_image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to=ecommerce.models.get_product_thumbnail_upload_path),
        ),
    ]