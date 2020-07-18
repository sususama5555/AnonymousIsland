# -*- coding: utf-8 -*-
"""
@File  :serializers.py
@Author:Sapphire
@Date  :2020/7/15 19:53
@Desc  :
"""
from rest_framework import serializers

from mood.models.comment import Comment
from mood.models.mood import Mood
from mood.models.user import User


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'


class MoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
