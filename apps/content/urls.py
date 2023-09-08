from django.urls import path, include
from rest_framework.routers import DefaultRouter

from content.serializers.like import LikeReelSerializer
from content.view.comment import CommentModelViewSet, CommentReelModelViewSet
from content.view.like import LikeReelModelViewSet, LikePostModelViewSet, LikeCommentModelViewSet
from content.view.post import PostModelViewSet
from content.view.reel import ReelModelViewSet

router = DefaultRouter()
router.register('posts', PostModelViewSet, 'posts'),
router.register('reel', ReelModelViewSet, 'reel'),
router.register('comment', CommentModelViewSet, 'comment'),
router.register('comment-reel', CommentReelModelViewSet, 'comment-reel'),
router.register('like-reel', LikeReelModelViewSet, 'like-reel'),
router.register('like-post', LikePostModelViewSet, 'like-post'),
router.register('like-comment', LikeCommentModelViewSet, 'like-comment'),
urlpatterns = [
    path('', include(router.urls))
]
