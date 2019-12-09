# 引入我们创建的表单类
# coding:utf-8
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from map.model.city import CityModel
from map.model.infodata import InfoModel,CarSellModel,CarServiceModel,CarMaintainModel
from rest_framework.views import APIView

class MapIndex(View):
    def get(self, request):
        datas = CityModel.objects.all()
        citys = []
        for data in datas:
            citys.append({'citycode':data.citycode})
        return render(request, 'map/index.html', context={'citys':citys})

    def post(self, request):
        return render(request, 'map/index.html')

class InsertInfoData(APIView):
    def get(self,request):
        datas = json.loads(request.GET['data'])
        for data in datas['pois']:
            try:
                CarMaintainModel.objects.create(id=data['id'],name=data['name'],
                                         type=data['type'],typecode=data['typecode'],
                                         biz_type=data['biz_type'],address=data['address'],
                                         locations=data['location'],tel=data['tel'],
                                         pname=data['pname'],cityname=data['cityname'],
                                         adname=data['adname'],remark='')
            except Exception as e:
                print('出现错误')
        return JsonResponse({'sucess':'插入成功'})

class InsertMapData(View):
    def get(self,request):
        datas = json.loads(request.GET['data'])
        for data in datas['pois']:
            try:
                InfoModel.objects.create(id=data['id'],name=data['name'],
                                         type=data['type'],typecode=data['typecode'],
                                         biz_type=data['biz_type'],address=data['address'],
                                         locations=data['location'],tel=data['tel'],
                                         pname=data['pname'],cityname=data['cityname'],
                                         adname=data['adname'],remark='')
            except Exception as e:
                print('出现错误')
        return JsonResponse({'sucess':'插入成功'})
    # def get(self,request):
    #     print('dssdsd')
    #     datas = json.loads(request.GET['data'])
    #     for data in datas['suggestion']['cities']:
    #         try:
    #             CityModel.objects.create(name=data['name'],num=data['num'],citycode=data['citycode'],adcode=data['adcode'])
    #         except Exception as e:
    #             print('出现错误')
    #     return JsonResponse({'sucess':'插入成功'})