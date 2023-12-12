# Generated by Django 4.2.6 on 2023-11-23 15:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_is_active_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='last_user_login',
        ),
        migrations.AddField(
            model_name='device',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'web'), (2, 'ios'), (3, 'android')], default=1),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_uuid',
            field=models.UUIDField(null=True, verbose_name='Device UUID'),
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='province',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(null=True, verbose_name='last seen date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, error_messages={'unique': 'A user with this mobile number already exists.'}, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$', 'Enter a valid mobile number.', 'invalid')], verbose_name='mobile number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer starting with a letter. Letters, digits and underscore only.', max_length=32, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z][a-zA-Z0-9_\\.]+$', 'Enter a valid username starting with a-z. This value may contain only letters, numbers and underscore characters.', 'invalid')], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.BooleanField(help_text='female is False, male is True, null is unset', null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='nick_name'),
        ),
        migrations.AlterModelTable(
            name='device',
            table='user_devices',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='user_profiles',
        ),
    ]
