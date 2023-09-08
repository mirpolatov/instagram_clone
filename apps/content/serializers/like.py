from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from content.models import LikeReel, LikePost, LikeComment


class LikeReelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = LikeReel
        fields = ('reel', 'user')


class LikePostSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = LikePost
        fields = ('post', 'user')


class LikeCommentSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = LikeComment
        fields = ('comment', 'user')
