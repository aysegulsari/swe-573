# Generated by Django 3.0.5 on 2020-06-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200618_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='usdaID',
            field=models.IntegerField(default=0),
        ),
    ]