# Generated by Django 3.0.5 on 2020-06-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_likeformenu_meal_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='menu_title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
