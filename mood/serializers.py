# -*- coding: utf-8 -*-
"""
@File  :serializers.py.py
@Author:Sapphire
@Date  :2020/7/15 19:53
@Desc  :
"""
from rest_framework import serializers

from .models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'
