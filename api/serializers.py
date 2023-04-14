from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(read_only=True,many=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model=Post
        fields=['id','title','body','author','category','tags','image','summary','created_at','updated_at']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields='__all__'

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields='__all__'	