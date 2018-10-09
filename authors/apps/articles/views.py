from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .serializers import ArticleSerializer
from .renderers import ArticleJSONRenderer
from .models import Article


class ArticleViewSet(ModelViewSet):

    renderer_classes = (ArticleJSONRenderer,)
    serializer_class = ArticleSerializer

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
