from rest_framework import serializers
from smapi.models import createPost

class CreatePostSerializer(serializers.ModelSerializer):
    # created_by = serializers.StringRelatedField()  # Show the username instead of user ID
    created_by = serializers.ReadOnlyField(source='created_by.name')  # Get the username instead of the User object
    class Meta:
        model=createPost
        fields="__all__"