from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from content.models import Post, Reel


class ReelModelSerializer(ModelSerializer):
    id = CharField(read_only=True)

    class Meta:
        model = Reel
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comments', 'id')


class UpdateReelModelSerializer(ModelSerializer):
    class Meta:
        model = Reel
        fields = 'caption', 'location'
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comment', 'id')

    def to_representation(self, instance):
        return ReelModelSerializer(instance).data
