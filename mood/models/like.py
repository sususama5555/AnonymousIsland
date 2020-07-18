from django.db import models
from django.utils.translation import ugettext as _

from mood.basic import CreateMixin, UpdateMixin, DeleteMixin
from mood.constants import *

# Create your models here.
from mood.managers import LikeManager
from mood.models.comment import Comment
from mood.models.mood import Mood
from mood.models.user import User


class MoodLike(DeleteMixin):
    mood = models.ForeignKey(Mood, verbose_name=_("心情"), related_name="likes", on_delete=models.CASCADE)
    Like_at = models.DateTimeField(verbose_name=_("点赞时间"), auto_now=True)
    user = models.ForeignKey(User, verbose_name=_("用户"), related_name="likes", on_delete=models.CASCADE, )

    class Meta:
        app_label = "mood"
        verbose_name = _("心情点赞")
        verbose_name_plural = _("心情点赞")

    def __str__(self):
        return "{}({})".format(self.user.username, self.mood.id)


class CommentLike(DeleteMixin):
    comment = models.ForeignKey(Comment, verbose_name=_("评论"), related_name="likes", on_delete=models.CASCADE)
    Like_at = models.DateTimeField(verbose_name=_("点赞时间"), auto_now=True)
    user = models.ForeignKey(User, verbose_name=_("用户"), related_name="likes", on_delete=models.CASCADE, )

    class Meta:
        app_label = "mood"
        verbose_name = _("评论点赞")
        verbose_name_plural = _("评论点赞")

    def __str__(self):
        return "{}({})".format(self.user.username, self.comment.id)
