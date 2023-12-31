from django.utils.decorators import method_decorator
from drf_yasg import utils, openapi
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from content.models import Reel
from content.serializers.reel import ReelModelSerializer, UpdateReelModelSerializer


@method_decorator(name='create', decorator=utils.swagger_auto_schema(manual_parameters=[openapi.Parameter(
    name='media',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    required=True,
    description='media'
)]))
class ReelModelViewSet(ModelViewSet):
    serializer_class = ReelModelSerializer
    parser_classes = (MultiPartParser,)
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return UpdateReelModelSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Reel.objects.filter(author=self.request.user.id)
        return queryset
