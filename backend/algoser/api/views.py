from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostsSerializer
from posts.models import Posts
from rest_framework import viewsets
from api.permissions import AuthorStaffOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (AuthorStaffOrReadOnly,)