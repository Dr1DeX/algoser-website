from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from api import views

app_name = 'api'



urlpatterns = [
    path('v1/token', TokenObtainPairView.as_view(), name='token_obtain'),
    path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/posts/', views.PostAPIList.as_view()),
    path('v1/posts/create/', views.PostAPICreate.as_view()),
    path('v1/post/<int:pk>/', views.PostAPIUpdate.as_view()),
    path('v1/postdelete/<int:pk>/', views.PostsAPIDestroy.as_view()),
]
