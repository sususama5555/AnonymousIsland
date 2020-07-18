# -*- coding: utf-8 -*-
"""
@File  :urls.py
@Author:Sapphire
@Date  :2020/7/15 20:07
@Desc  :
"""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import MoodViewSet, MyMoodViewSet, CommentViewSet, UserViewSet

routers = DefaultRouter(trailing_slash=True)

routers.register(r"moods", MoodViewSet)
# routers.register(r"my_moods", MyMoodViewSet)
routers.register(r"comments", CommentViewSet)
routers.register(r"user", UserViewSet)

urlpatterns = routers.urls
