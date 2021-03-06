# Generated by Django 3.0.7 on 2020-06-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200622_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='like',
            name='user_profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfileInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='', max_length=1500),
        ),
    ]
