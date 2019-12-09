from django.db import models

class CityModel(models.Model):
    name = models.CharField('名称', max_length=255, default='', null=True,blank=True) #用户名
    num = models.CharField('编号', max_length=255, default='', null=True,blank=True)
    citycode = models.CharField('城市编码',primary_key=True, max_length=255, default='') #用户ID
    adcode = models.EmailField('邮政编码',max_length=255, default='', null=True,blank=True)

    def __str__(self):
        return self.name
