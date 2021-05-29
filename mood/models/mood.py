import os
import datetime

from django.db import models
from django.utils.translation import ugettext as _

from config.settings import MEDIA_ROOT
from mood.basic import CreateMixin, UpdateMixin, DeleteMixin
from mood.constants import *

# Create your models here.
from mood.managers import MoodManager
from mood.models.user import User


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    now = datetime.datetime.today().strftime("%y%m%d-%H%S")
    filename = '{}{}.{}'.format(instance.user.openid, now, ext)
    return filename


class Mood(CreateMixin, UpdateMixin, DeleteMixin):
    content = models.TextField(verbose_name=_("内容"), max_length=LEN_X_LONG)
    image = models.ImageField(verbose_name=_("附图"), max_length=LEN_X_LONG, upload_to=user_directory_path, null=True,
                              blank=True)
    click_counter = models.IntegerField(verbose_name=_("点击数"), default=EMPTY_INT)
    comment_counter = models.IntegerField(verbose_name=_("评论数"), default=EMPTY_INT)
    like_counter = models.IntegerField(verbose_name=_("点赞数"), default=EMPTY_INT)
    user = models.ForeignKey(User, verbose_name=_("用户"), related_name="mood", on_delete=models.CASCADE,)

    objects = MoodManager()

    class Meta:
        ordering = ("-create_at",)
        app_label = "mood"
        verbose_name = _("心情")
        verbose_name_plural = _("心情")

    def __str__(self):
        return str(self.id)

    def click_increase(self):
        """点击心情，点击数增加"""
        self.click_counter += 1
        self.save()

    def comment_increase(self):
        """评论心情，点击数增加"""
        self.comment_counter += 1
        self.save()



