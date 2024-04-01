from rest_framework import serializers
from posts.models import Posts


class PostsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    class Meta:
        model = Posts
        fields = ('author', 'category', 'title', 'text', 'update_date')

