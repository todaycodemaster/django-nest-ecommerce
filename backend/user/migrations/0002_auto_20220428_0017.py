# Generated by Django 3.2 on 2022-04-27 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email_verification_otp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email_verification_otp_expired_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_email_verified',
        ),
    ]