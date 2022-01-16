from rest_framework import serializers
from writer.models import Blogpost

class BlogPostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['id','blog_title','blog_content']

class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['id','blog_title','blog_content']

##adding comments

