from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import ArticleSerializer, CategorySerializer, TagSerializer

from .renderers import ArticleJSONRenderer, CategoryJSONRenderer, TagJSONRenderer
from .models import Article, Category
from taggit.models import Tag


class CategoryViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CategoryJSONRenderer,)
    serializer_class = CategorySerializer
    lookup_field = "slug"

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
    
    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            slug=self.kwargs.get("slug")
        )
    
    def create(self, request, *args, **kwargs):
        category = Category.objects.filter(
            name=request.data.get("name")
        ).exists()
        if category:
            raise ValidationError(
                "Category already exists"
            )
        return super().create(request, *args, **kwargs)
            
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @detail_route(methods=['get'])
    def articles(self, request, slug=None):
        articles = Article.objects.filter(category__slug=slug)
        serializer = ArticleSerializer(articles, many=True)
        return Response({slug: serializer.data}, status.HTTP_200_OK)


class ArticleViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (ArticleJSONRenderer,)
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset
    
    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            slug=self.kwargs.get("slug")
        )
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (TagJSONRenderer,)
    serializer_class = TagSerializer
    lookup_field = "slug"
    
    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset
