# Generated by Django 2.2.7 on 2019-12-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='名称')),
                ('num', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='编号')),
                ('citycode', models.CharField(default='', max_length=255, primary_key=True, serialize=False, verbose_name='城市编码')),
                ('adcode', models.EmailField(blank=True, default='', max_length=255, null=True, verbose_name='邮政编码')),
            ],
        ),
    ]
