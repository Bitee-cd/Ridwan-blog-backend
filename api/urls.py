from django.urls import path,include
from .views import *

urlpatterns = [
    path('',getRoutes,name="routes"),
    path('posts/',all_posts , name="post" ),
    path('post-detail/<str:pk>/',post_detail,name="post"),
    path('categories/',all_categories,name="category"),
    path('category-posts/<str:category>/',category_posts,name="category"),
    path('authors/',all_authors,name="author"),
    path('author-details/<str:pk>/',author_detail,name="author"),
    path('author-posts/<str:author>/',author_posts,name="author"),
    path('newsletter/',create_newsletter,name="newsletter")

]
