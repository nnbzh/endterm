from rest_framework import viewsets, mixins

from app.posts import serializers
from app.posts.models import Post


class PostsViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = serializers.PostsSerializer
    queryset = Post.objects.all()
