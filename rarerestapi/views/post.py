"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarerestapi.models.post import Post
from rarerestapi.models.rare_users import RareUser
from rarerestapi.models.categories import Categories


class PostView(ViewSet):
    """Post view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Post"""

        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all Posts """
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """
        author = RareUser.objects.get(user=request.auth.user)
        category_id = Categories.objects.get(pk=request.data["category_id"])

        post = Post.objects.create(
            user_id=author,
            category_id=category_id,
            title=request.data["title"],
            publication_date=request.data["publication_date"],
            image_url=request.data["image_url"],
            content=request.data["content"],
            approved=request.data["approved"]
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a post

        Returns:
            Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        post.approved = request.data["approved"]

        author = RareUser.objects.get(pk=request.data["author"])
        post.user_id = author
        category_id = Categories.objects.get(pk=request.data["category_id"])
        post.category_id = category_id
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts """
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'category_id', 'title',
                  'publication_date', 'image_url', 'content', 'approved')
