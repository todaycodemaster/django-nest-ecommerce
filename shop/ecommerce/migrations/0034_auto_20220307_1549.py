# Generated by Django 3.2 on 2022-03-07 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0033_auto_20220306_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engravingtechnique',
            name='protect_import',
        ),
        migrations.RemoveField(
            model_name='product',
            name='protect_import',
        ),
    ]
