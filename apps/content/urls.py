from django.urls import path, include
from rest_framework.routers import DefaultRouter

from content.view.post import PostModelViewSet
from content.view.reel import ReelModelViewSet

router = DefaultRouter()
router.register('posts', PostModelViewSet, 'posts')
router.register('reel', ReelModelViewSet, 'reel')
urlpatterns = [
    path('', include(router.urls))
]
