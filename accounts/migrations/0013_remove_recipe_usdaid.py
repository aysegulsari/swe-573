# Generated by Django 3.0.5 on 2020-06-18 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_recipe_usdaid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='usdaID',
        ),
    ]