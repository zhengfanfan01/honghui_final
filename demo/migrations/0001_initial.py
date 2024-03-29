# Generated by Django 2.2.3 on 2019-09-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('phone', models.CharField(max_length=14, verbose_name='电话')),
                ('personal_info', models.CharField(max_length=100, verbose_name='职位或者公司名称')),
                ('message_c', models.CharField(max_length=200, verbose_name='留言信息')),
                ('publish', models.DateTimeField()),
            ],
            options={
                'verbose_name': '留言信息',
                'verbose_name_plural': '留言信息',
                'db_table': 'message',
            },
        ),
    ]
