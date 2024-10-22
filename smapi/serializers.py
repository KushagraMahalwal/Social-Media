from rest_framework import serializers
from smapi.models import createPost,comment

class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.ReadOnlyField(source='commented_by.name')
    class Meta:
        model= comment
        # fields="__all__"
        fields = ['comm','commented_by']


class CreatePostSerializer(serializers.ModelSerializer):
    # created_by = serializers.StringRelatedField()  # Show the username instead of user ID
    comments=CommentSerializer(many=True,read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.name')  # Get the username instead of the User object

    class Meta:
        model=createPost
        fields="__all__"
        # exclude=('post',)


