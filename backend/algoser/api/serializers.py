from rest_framework import serializers
from posts.models import Posts


class PostsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    class Meta:
        model = Posts
        fields = ('author', 'category', 'title', 'text', 'update_date')

