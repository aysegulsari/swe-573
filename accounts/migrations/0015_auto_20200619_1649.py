# Generated by Django 3.0.5 on 2020-06-19 13:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200618_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='providerName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
