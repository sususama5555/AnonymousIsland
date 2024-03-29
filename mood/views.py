# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from mood.models.mood import Mood
from .models.comment import Comment
from .models.user import User
from .serializers import MoodSerializer, MoodListSerializer, CommentSerializer, UserSerializer


class MoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.filter(is_deleted=False)
    serializer_class = MoodSerializer

    ordering_fields = "__all__"

    def list(self, request, *args, **kwargs):
        """心情列表"""

        self.serializer_class = MoodListSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """心情详情"""

        instance = self.get_object()
        # 点击数增加
        instance.click_increase()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super(MoodViewSet, self).create(request, *args, **kwargs)


class MyMoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.filter()
    serializer_class = MoodListSerializer

    ordering_fields = "__all__"

    def get_queryset(self):
        return self.queryset.filter(user__openid=self.request.GET.get("openid"))


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_deleted=False)
    serializer_class = CommentSerializer

    filter_fields = {
        "mood_id": ["exact"],
    }
    ordering_fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(openid=request.data.get("openid"))
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except User.DoesNotExist:
            return super(UserViewSet, self).create(request, *args, **kwargs)


