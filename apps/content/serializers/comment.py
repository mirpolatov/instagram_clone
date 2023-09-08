from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from content.models import Comment, CommentReel


class CommentModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('comment', 'post', 'user')


class CommentReelModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = CommentReel
        fields = ('comment', 'reel', 'user')
