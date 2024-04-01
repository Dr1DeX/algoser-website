from api.serializers import PostsSerializer
from posts.models import Posts
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
