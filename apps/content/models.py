from django.db import models
from django.db.models import CASCADE
from users.models import UserProfile


# class Post(models.Model):
#     image = models.ImageField(upload_to="post_img/", blank=True, null=True)
#     video = models.FileField(upload_to="post_mp4/", blank=True, null=True)
#     body = models.TextField(null=True)
#     location = models.CharField(max_length=75, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     to_user = models.ForeignKey(UserProfile, CASCADE, related_name="my_post")
#
#     def __str__(self):
#         return self.created_at
#
#
# class Reel(models.Model):
#     video = models.FileField(upload_to='reel_mp4/', blank=True)
#     body = models.TextField(null=True)
#     location = models.CharField(max_length=75, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(UserProfile)
#     comments = models.ManyToManyField(UserProfile)
#     to_user = models.ForeignKey(UserProfile, CASCADE, related_name="my_reel")
#
#     def __str__(self):
#         return self.created_at
