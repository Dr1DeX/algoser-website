from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostsSerializer
from posts.models import Posts
from rest_framework import generics
from api.permissions import AuthorStaffOrReadOnly, OwnerUserOrReadOnly, AdminOrReadOnly


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
    serializer_class = PostsSerializer
    permission_classes = (OwnerUserOrReadOnly,)


class PostsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (AdminOrReadOnly,)
