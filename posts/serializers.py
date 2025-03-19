from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # he author is also 1 since we used a superuser account, which was the first one created, 
    # and since author is a ForeignKey to our custom user model, DRF defaults to serializing it by its primary key
    # author = serializers.ReadOnlyField(source='author.username')

    #another solution 
    author = serializers.SlugRelatedField(  # new
        queryset=get_user_model().objects.all(), slug_field="username"
    )
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )
