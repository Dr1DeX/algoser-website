from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostsSerializer, RegisterSerializer
from posts.models import Posts
from rest_framework import generics
from api.permissions import AuthorStaffOrReadOnly, OwnerUserOrReadOnly, AdminOrReadOnly

User = get_user_model()


class PostAPIList(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (AuthorStaffOrReadOnly,)


class PostAPICreate(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    parser_classes = [FileUploadParser]
    serializer_class = PostsSerializer
    permission_classes = (OwnerUserOrReadOnly,)


class PostsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (AdminOrReadOnly,)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
