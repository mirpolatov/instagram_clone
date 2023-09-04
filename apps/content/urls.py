from django.urls import path, include
from rest_framework.routers import DefaultRouter

from content.view.post import PostModelViewSet

router = DefaultRouter()
router.register('p', PostModelViewSet, 'posts')
urlpatterns = [
    path('', include(router.urls))
]