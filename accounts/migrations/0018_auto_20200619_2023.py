# Generated by Django 3.0.5 on 2020-06-19 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200619_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='providerName',
            new_name='provider_name',
        ),
    ]