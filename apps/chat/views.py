from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chat.models import UserChat
from chat.serializer import ChatModelSerializer


# Create your views here.


class ChatViewSet(ModelViewSet):
    serializer_class = ChatModelSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserChat.objects.all()
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch', 'delete')
