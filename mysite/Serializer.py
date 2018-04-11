#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SundayCoder-俊勇
# @File    : Serializer.py
from rest_framework.serializers import ModelSerializer
from mysite.models import User
class UserSerializer(ModelSerializer):
    # 设置序列化
    class Meta:
        model = User
        fields = "__all__"
