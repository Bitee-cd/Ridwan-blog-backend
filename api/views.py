from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import status

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
        "author posts":"{baseUrl}/author-posts/{author-id}",
        "newsletter":"{baseUrl}/newsletter",
        "get all newsletter":"{baseUrl}/newsletter",
        "get books":"{baseUrl}/books",
        "get Medicals":"{baseUrl}/medicals",

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
    serializer=CategorySerializer(category,many=True)
    return Response(serializer.data)

@api_view(['GET'])	
def category_posts(request,category):
    posts=Post.objects.filter(category=category).order_by('publish')
    serializer=PostSerializer(posts,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_authors(request):
    author= Author.objects.all()
    serializer=AuthorSerializer(author,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def author_detail(request,pk):
    author=Author.objects.get(id=pk)
    serializer=AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['GET'])	
def author_posts(request,author):
    posts=Post.objects.filter(author=author).order_by('publish')
    paginator = PageNumberPagination()
    result = paginator.paginate_queryset(posts,request)
    serializer=PostSerializer(result,many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])	
def books(request):
    books=Book.objects.all()
    paginator = PageNumberPagination()
    result = paginator.paginate_queryset(books,request)
    serializer=BookSerializer(result,many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])	
def medicals(request):
    medicals=Medical.objects.all()
    paginator = PageNumberPagination()
    result = paginator.paginate_queryset(medicals,request)
    serializer=MedicalSerializer(result,many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST','GET'])
def create_newsletter(request):
    if request.method == 'POST':
        serializer = NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success":True,
                },status=status.HTTP_201_CREATED)
        return Response({
            "success":False,
        },serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        newsletter=NewsLetter.objects.all()
        serializer=NewsLetterSerializer(newsletter,many=True)
        return Response(serializer.data)