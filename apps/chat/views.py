from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from chat.models import UserChat
from chat.serializer import ChatModelSerializer


# Create your views here.


class ChatViewSet(ModelViewSet):
    serializer_class = ChatModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_queryset(self):
        queryset = UserChat.objects.filter(user_id=self.request.user.id)
        return queryset
