from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Mood
from .serializers import MoodSerializer


class MoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
