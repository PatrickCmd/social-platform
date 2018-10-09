from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article

        extra_kwargs = {
            'slug': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        fields = ('id', 'author', 'title', 'slug', 'description', 'body',
                  'image', 'created_at', 'updated_at')
