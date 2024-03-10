from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'post_type', 'date_posted', 'author']