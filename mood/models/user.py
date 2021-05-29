# -*- coding: utf-8 -*-
"""
@File  :user.py
@Author:Sapphire
@Date  :2020/7/15 19:53
@Desc  :
"""

from django.db import models
from django.utils.translation import ugettext as _

from mood.basic import CreateMixin, UpdateMixin, DeleteMixin
from mood.constants import *

# Create your models here.
from mood.managers import UserManager


class User(CreateMixin, UpdateMixin, DeleteMixin):
    openid = models.IntegerField(verbose_name=_("WX唯一ID"), default=EMPTY_INT, primary_key=True)
    username = models.CharField(verbose_name=_("用户名"), max_length=LEN_SHORT)
    fakename = models.CharField(verbose_name=_("用户匿名"), max_length=LEN_SHORT)

    class Meta:
        ordering = ("-create_at",)
        app_label = "mood"
        verbose_name = _("用户")
        verbose_name_plural = _("用户")
