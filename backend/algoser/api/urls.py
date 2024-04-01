from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api import views

app_name = 'api'

urlpatterns = [
    path('v1/token', views.MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
