from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from api import views

app_name = 'api'

router = DefaultRouter()
router.register('v1/posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('v1/token', TokenObtainPairView.as_view(), name='token_obtain'),
    path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
