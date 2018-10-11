from rest_framework import serializers

from .models import Article, Category
from taggit.models import Tag

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagListSerializerField()

    class Meta:
        model = Article

        extra_kwargs = {
            'slug': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        fields = ('id', 'author', 'category', 'title', 'slug', 'description',
                  'body', 'image', 'tags', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # articles = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="articles:article-detail"
    # )
    # articles = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category

        extra_kwargs = {
            'slug': {'read_only': True},
        }
        fields = ('id', 'author', 'name', 'slug')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')
