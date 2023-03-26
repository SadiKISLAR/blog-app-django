from rest_framework import serializers
from django.db.models import Q
from .models import (
    Blog,
    Comment,
    Like,
    BlogView
    )

from users.serializers import ProfileSerializer

class LikeSerializer(serializers.ModelSerializer):

    user= serializers.StringRelatedField()
    user_id= serializers.IntegerField(read_only=True)
    blog= serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "user_id",
            "blog",
            "blog_id"
        )

class CommentSerializer(serializers.ModelSerializer):

    user = ProfileSerializer(source='user.profile', read_only=True)
    user_id = serializers.IntegerField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comment

        fields = [
            "id",
            "user_id",
            "user",
            "blog_id",
            "blog",
            "content",
            "publish_date"
        ]

class BlogSerializer(serializers.ModelSerializer):

    like = LikeSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField()
    
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "image" ,
            "category",
            "status" ,
            "published_date",
            "updated_date",
            "author_id",
            "author",
            "like",
            "like_count",
            "has_liked",
            "comments",
            "get_view_count",
            ]
        
    def get_like_count(self, obj):
        return obj.like.count()

    def get_has_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Like.objects.filter(user=request.user.id, blog=obj).exists():
                return True
            return False 