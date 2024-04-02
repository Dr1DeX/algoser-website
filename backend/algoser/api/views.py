from api.serializers import PostsSerializer
from posts.models import Posts
from rest_framework import viewsets
from api.permissions import AuthorStaffOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    permission_classes = (AuthorStaffOrReadOnly,)
