from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField



# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    about_me = RichTextField()
    profile_image = models.ImageField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkdn = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    whatsapp = models.CharField(blank=True, null=True, max_length=15)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title=models.CharField(max_length=100)
    body = RichTextUploadingField(default="Empty Content")
    author=models.ForeignKey(Author,related_name="author",on_delete=models.CASCADE)
    category= models.ForeignKey(Category,related_name="category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    daily_views = models.IntegerField(default=0, blank=False)
    tags = models.ManyToManyField(Tags, related_name="tags", default=[1])
    publish = models.BooleanField(default=False)
    summary = RichTextUploadingField(default='Empty Content')
    

    def __str__(self):
        return self.title

class NewsLetter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    def __str__(self):
        return self.name