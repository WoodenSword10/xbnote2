# Generated by Django 3.2.6 on 2021-09-01 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_rename_name_user_info_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('classify', models.CharField(default='', max_length=10, verbose_name='分类')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_info')),
            ],
            options={
                'verbose_name': '笔记',
                'verbose_name_plural': '笔记',
                'db_table': 'Note',
            },
        ),
    ]
