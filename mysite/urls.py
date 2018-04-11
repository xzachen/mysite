#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SundayCoder-俊勇
# @File    : urls.py
from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    # 注册的路由 POST
    path('register', views.register, name='register'),

]
