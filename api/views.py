from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes ={
        "all posts":"{baseUrl}/posts/",
        "single post":"{baseUrl}/post-detail/{id}/",
        "all categories":"{baseUrl}/categories/",
        "category posts":"{baseUrl}/category-posts/{category-id}",
        "all authors":"{baseUrl}/authors/",
        "single author":"{baseUrl}/author-detail/{id}",
        "author posts":"{baseUrl}/author-posts/{author-id}"

    }
    return Response(routes)

@api_view(['GET'])
def all_posts(request):
    posts = Post.objects.filter(publish = True).order_by('publish')
    paginator = PageNumberPagination()
    result = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    serializers=PostSerializer(post)
    return Response(serializers.data)

@api_view(['GET'])
def all_categories(request):
    category= Category.objects.all()
    serializers=CategorySerializer(category,many=True)
    return Response(serializers.data)

@api_view(['GET'])	
def category_posts(request,category):
    posts=Post.objects.filter(category=category).order_by('publish')
    serializers=PostSerializer(posts,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def all_authors(request):
    author= Author.objects.all()
    serializers=AuthorSerializer(author,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def author_detail(request,pk):
    author=Author.objects.get(id=pk)
    serializers=AuthorSerializer(author)
    return Response(serializers.data)

@api_view(['GET'])	
def author_posts(request,author):
    posts=Post.objects.filter(author=author).order_by('publish')
    serializers=PostSerializer(posts,many=True)
    return Response(serializers.data)