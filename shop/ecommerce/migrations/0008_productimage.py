# Generated by Django 3.2 on 2021-12-29 03:58

from django.db import migrations, models
import django.db.models.deletion
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20211229_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=ecommerce.models.get_product_image_upload_path)),
                ('slug', models.SlugField(allow_unicode=True, editable=False, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belongs_to_product', to='ecommerce.product')),
            ],
            options={
                'db_table': 'ecommerce_product_image',
                'ordering': ['-created_at'],
            },
        ),
    ]
