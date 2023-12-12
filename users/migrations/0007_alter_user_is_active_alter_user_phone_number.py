# Generated by Django 4.2.6 on 2023-11-23 14:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='user must be active, un select this instead deleting accounted', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, error_messages={'unique': 'user with that phone number already exist'}, help_text='Required. inter a phone number start with 98', null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$')], verbose_name='phone number'),
        ),
    ]