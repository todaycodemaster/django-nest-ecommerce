# Generated by Django 3.2 on 2022-02-28 15:50

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_alter_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_thumbnail_image',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product_image',
            field=models.FileField(blank=True, null=True, upload_to=ecommerce.models.get_product_image_upload_path),
        ),
    ]
