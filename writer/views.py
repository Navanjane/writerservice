from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from writer.models import Blogpost
from writer.serializers import BlogPostWriteSerializer,BlogPostListSerializer
from .producer import publish


# Create your views here.

@api_view(['POST'])
def writepost(request):
    serializer = BlogPostWriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        publish('blog_created', serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listposts(request):
    posts = Blogpost.objects.all()
    serializer = BlogPostListSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def readpost(request,pk):
    post = Blogpost.objects.get(id=pk)
    serializer = BlogPostListSerializer(post)
    return Response(serializer.data)

