# Generated by Django 3.2 on 2022-01-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_remove_color_parent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='jhk_size',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]