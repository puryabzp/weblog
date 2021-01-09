from abc import ABC

from rest_framework import serializers
from .models import Post, User, Comment,Category,CommentLike,PostSetting
from account.serializer import UserSerializer


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    slug = serializers.SlugField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    publish_time = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.id = validated_data.get('id', instance.id)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.create_at = validated_data.get('create_at', instance.create_at)
        instance.update_at = validated_data.get('update_at', instance.update_at)
        instance.publish_time = validated_data.get('publish_time', instance.publish_time)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    author_detail = UserSerializer(source='author', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSetting
        fields = '__all__'