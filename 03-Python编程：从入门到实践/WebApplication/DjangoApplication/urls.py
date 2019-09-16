# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :        Liangz
   Date：          2018/10/29
-------------------------------------------------
   Change Activity:
                   2018/10/29:
-------------------------------------------------
"""
__author__ = 'Liangz'


from django.conf.urls import url
from . import views


urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
]
