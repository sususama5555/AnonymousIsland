from django.contrib import admin

# Register your models here.
from mood.models.mood import Mood

admin.site.register(Mood)
