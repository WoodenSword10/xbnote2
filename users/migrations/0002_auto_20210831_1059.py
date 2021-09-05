# Generated by Django 3.2.6 on 2021-08-31 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='res_time',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='user_info',
            name='updated_time',
            field=models.DateField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
