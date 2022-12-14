# Generated by Django 3.2 on 2022-03-05 12:16

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0031_alter_product_product_thumbnail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_thumbnail_image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=ecommerce.models.get_product_thumbnail_upload_path),
        ),
    ]
