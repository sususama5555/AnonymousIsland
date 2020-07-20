from django.contrib import admin

# Register your models here.
from mood.models.mood import Mood
from mood.models.comment import Comment
from mood.models.user import User

admin.site.register(Mood)
admin.site.register(Comment)
admin.site.register(User)
