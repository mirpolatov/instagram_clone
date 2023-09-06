from django.db import models
from django.db.models import CASCADE


# Create your models here.
class UserChat(models.Model):
    to_user = models.ForeignKey('users.UserProfile', CASCADE, 'messages')
    user_id = models.ForeignKey('users.UserProfile', CASCADE, 'my_messages')
    # user_image = models.ForeignKey('users.UserProfile', on_delete=CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)
    text = models.TextField(null=True,blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.to_user
