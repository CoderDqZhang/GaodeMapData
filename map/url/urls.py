from django.conf.urls import url
from map.view import map_view


urlpatterns = [
    url(r'index', map_view.MapIndex.as_view()),
    url(r'insert', map_view.InsertMapData.as_view()),
    url(r'insertinfo', map_view.InsertInfoData.as_view()),
]