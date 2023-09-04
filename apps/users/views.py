from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .models import UserProfile
from .serializers import UserProfileSerializer, UserFollowingModelSerializer, UserFollowModelSerializer


class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    # permission_classes = True
    serializer_class = UserProfileSerializer
    parser_classes = [MultiPartParser]


class UserFollowModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserFollowModelSerializer
    http_method_names = ('get', 'post')

    def get_serializer_class(self):
        if self.action == 'create':
            return UserFollowingModelSerializer
        return super().get_serializer_class()
