from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from chat.models import UserChat


class ChatModelSerializer(ModelSerializer):
    user_id = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = UserChat
        fields = ('to_user', 'image', 'video', 'text', 'user_id')
