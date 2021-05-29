
from django.db import models
from django.utils.translation import ugettext as _

from mood.basic import CreateMixin, UpdateMixin, DeleteMixin
from mood.constants import *

# Create your models here.
from mood.managers import CommentManager
from mood.models.mood import Mood
from mood.models.user import User


class Comment(CreateMixin, UpdateMixin, DeleteMixin):
    content = models.TextField(verbose_name=_("评论内容"), max_length=LEN_X_LONG)
    click_counter = models.IntegerField(verbose_name=_("点击数"), default=EMPTY_INT)
    like_counter = models.IntegerField(verbose_name=_("点赞数"), default=EMPTY_INT)
    mood = models.ForeignKey(Mood, verbose_name=_("心情"), related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("用户"), related_name="comments", on_delete=models.CASCADE,)

    objects = CommentManager()

    class Meta:
        ordering = ("-create_at",)
        app_label = "mood"
        verbose_name = _("评论")
        verbose_name_plural = _("评论")

    def __str__(self):
        return str(self.id)




