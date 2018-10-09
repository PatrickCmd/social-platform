import json

from rest_framework.renderers import JSONRenderer

from .models import Article


class ArticleJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # deleting article data returned is none
        if data is None:
            return json.dumps({
                'articles': "deleted from database"
            })
        errors = None
        if not isinstance(data, list) and data.get('errors'):
            errors = data.get('errors', None)

        if errors is not None:
            return super(ArticleJSONRenderer, self).render(data)
        
        if isinstance(data, list):
            return json.dumps({
                'articles': data,
                'articlesCount': Article.objects.count()
            })
        else:
            return json.dumps({
                'article': data
            })
