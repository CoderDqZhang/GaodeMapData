# Generated by Django 2.2.7 on 2019-12-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.CharField(default='', max_length=255, primary_key=True, serialize=False, verbose_name='ID名称')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='店名')),
                ('type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='分类')),
                ('typecode', models.CharField(default='', max_length=255, verbose_name='大类标识')),
                ('biz_type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='主要用途')),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='地址')),
                ('locations', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='经纬度')),
                ('tel', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='电话号码')),
                ('pname', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='省份')),
                ('cityname', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='城市')),
                ('adname', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='区县')),
                ('remark', models.CharField(default='', max_length=255, verbose_name='大类标识')),
            ],
        ),
    ]