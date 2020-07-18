# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from .constants import LEN_NORMAL
from . import managers


class CreateMixin(models.Model):
    create_at = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)

    class Meta:
        app_label = "mood"
        abstract = True


class UpdateMixin(models.Model):
    update_at = models.DateTimeField(verbose_name=_("更新时间"), auto_now=True)

    class Meta:
        app_label = "mood"
        abstract = True


class DeleteMixin(models.Model):
    is_deleted = models.BooleanField(verbose_name=_("是否软删除"), default=False)

    _objects = models.Manager()
    objects = managers.Manager()

    class Meta:
        app_label = "mood"
        abstract = True

    def delete(self, using=None):
        self.is_deleted = True
        self.save()

    def hard_delete(self, using=None):
        super(DeleteMixin, self).delete()
