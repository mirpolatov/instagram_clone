from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from content.models import LikeReel, LikePost, LikeComment
from content.serializers.like import LikeReelSerializer, LikePostSerializer, LikeCommentSerializer


class LikeReelModelViewSet(ModelViewSet):
    serializer_class = LikeReelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = LikeReel.objects.all()
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch')


class LikePostModelViewSet(ModelViewSet):
    serializer_class = LikePostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = LikePost.objects.all()
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch')


class LikeCommentModelViewSet(ModelViewSet):
    serializer_class = LikeCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = LikeComment.objects.all()
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch')
