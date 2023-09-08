from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from content.models import Comment, CommentReel
from content.serializers.comment import CommentModelSerializer, CommentReelModelSerializer


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_queryset(self):
        queryset = Comment.objects.filter(user=self.request.user.id)
        return queryset


class CommentReelModelViewSet(ModelViewSet):
    serializer_class = CommentReelModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_queryset(self):
        queryset = CommentReel.objects.filter(user=self.request.user.id)
        return queryset
