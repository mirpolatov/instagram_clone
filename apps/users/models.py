from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey


class UserProfile(AbstractUser):
    fullname = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image/',
                              default='https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg')
    bio = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    followers = models.ManyToManyField('self', 'my_followers', symmetrical=False)
    following = models.ManyToManyField('self', 'my_following', symmetrical=False)

    @property
    def following_count(self):
        return self.following.count()

    @property
    def followers_count(self):
        return self.followers.count()
