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

routers.register(r"moods", MoodViewSet, basename="moods")
routers.register(r"comments", CommentViewSet, basename="comments")
routers.register(r"users", UserViewSet, basename="users")
routers.register(r"my_moods", MyMoodViewSet, basename="my_moods")

urlpatterns = routers.urls
