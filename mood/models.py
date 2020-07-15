import os
import datetime

from django.db import models
from django.utils.translation import ugettext as _

from anonymous_mood.settings import MEDIA_ROOT
from .basic import CreateMixin, UpdateMixin, DeleteMixin
from .constants import *

# Create your models here.
from .managers import MoodManager


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    now = datetime.datetime.today().strftime("%y%m%d-%H%S")
    filename = '{}{}.{}'.format(instance.creator, now, ext)
    return filename


class Mood(CreateMixin, UpdateMixin, DeleteMixin):
    content = models.TextField(verbose_name=_("内容"), max_length=LEN_X_LONG)
    image = models.ImageField(verbose_name=_("附图"), max_length=LEN_X_LONG, upload_to=user_directory_path, null=True,
                              blank=True)
    click_counter = models.IntegerField(verbose_name=_("点击数"), default=EMPTY_INT)
    collect_counter = models.IntegerField(verbose_name=_("收藏数"), default=EMPTY_INT)
    like_counter = models.IntegerField(verbose_name=_("点赞数"), default=EMPTY_INT)

    objects = MoodManager()

    class Meta:
        ordering = ('create_at',)
        app_label = 'mood'
        verbose_name = _("心情")
        verbose_name_plural = _("心情")

    def __str__(self):
        return str(self.id)
