from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.users.views import UserProfileModelViewSet
from users.views import UserFollowModelViewSet

router = DefaultRouter()
router.register('users', UserProfileModelViewSet, basename="users")
router.register('follow', UserFollowModelViewSet, basename="follow")

urlpatterns = [
    path('', include(router.urls)),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
