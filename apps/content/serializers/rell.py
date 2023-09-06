from collections import OrderedDict

from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ListField, SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import ModelSerializer

from content.models import file_ext_validator, Post, Media


class PostModelSerializer(ModelSerializer):
    id = CharField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comments', 'id')


class UpdatePostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'caption', 'location'
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comment', 'id')

    def to_representation(self, instance):
        return PostModelSerializer(instance).data
