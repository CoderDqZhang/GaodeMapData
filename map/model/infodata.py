from django.db import models

class InfoModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name


class ShopingModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name


class CarServiceModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class CarSellModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class CarMaintainModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class MotoServiceModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class LifeServiceModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class SportServiceModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class DoctorServiceModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class HotellServiceModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class TripModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class HouseModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class GovModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class ArticleModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class rafficModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class inancialModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name

class CompanyModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name


class RoadModel(models.Model):

    id = models.CharField('ID名称',primary_key=True, max_length=255, default='') #用户名
    name = models.CharField('店名', max_length=255, default='', null=True,blank=True)
    type = models.CharField('分类', max_length=255, default='', null=True,blank=True)
    typecode = models.CharField('大类标识', max_length=255, default='') #用户ID
    biz_type = models.CharField('主要用途',max_length=255, default='', null=True,blank=True)
    address = models.CharField('地址', max_length=255, default='', null=True, blank=True)  # 用户名
    locations = models.CharField('经纬度', max_length=255, default='', null=True, blank=True)
    tel = models.CharField('电话号码',  max_length=255, default='', null=True, blank=True)  # 用户ID
    pname = models.CharField('省份', max_length=255, default='', null=True, blank=True)
    cityname = models.CharField('城市', max_length=255, default='', null=True, blank=True)  # 用户名
    adname = models.CharField('区县', max_length=255, default='', null=True, blank=True)
    remark = models.CharField('大类标识', max_length=255, default='')  # 用户ID
    def __str__(self):
        return self.name