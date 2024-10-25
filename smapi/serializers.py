from rest_framework import serializers
from smapi.models import createPost,comment
from django.contrib.auth.models import User
 

class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.ReadOnlyField(source='commented_by.name')
    class Meta:
        model= comment
        fields = ['id','comm','commented_by']


class CreatePostSerializer(serializers.ModelSerializer):
    # created_by = serializers.StringRelatedField()  # Show the username instead of user ID
    comments=CommentSerializer(many=True,read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.name')  # Get the username instead of the User object
    liked_by = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')  # Show usernames of users who liked
    
    class Meta:
        model=createPost
        fields="__all__"

class LikePostSerializer(serializers.ModelSerializer):
    post_id=serializers.IntegerField()

