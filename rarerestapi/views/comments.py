from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from tomlkit import comment
from rarerestapi.models import Comment
from rarerestapi.models import Post
from rarerestapi.models.post import Post
from rarerestapi.models.rare_users import RareUser
from rarerestapi.models.categories import Categories

class CommentView(ViewSet):
    """Comments"""
    def retrieve(self, request,pk):
        
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def list(sefl,request):
        
        comment = Comment.objects.all()
        serializer = CommentSerializer
        return Response(serializer.data)
    
    def create(self,request):
        
        post = Post.objects.get(pk=request.data["post_id"])
        author = RareUser.objects.get(user=request.auth.user)
        
        comment = Comment.objects.create(
            post_id=post,
            user_id=author,
            content=request.data["content"],
            created_on=request.data["datetime"]
        )
        serializer = CommentSerializer(post)
        return Response(serializer.data)
    
        
    
    
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for posts """
    class Meta:
        model = Comment
        fields = ('id', 'post_id','author_id','content','created_on')