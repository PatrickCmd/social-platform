from django.urls import path, re_path

from .views import ArticleViewSet

urlpatterns = [
    path('articles/', ArticleViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'articles/(?P<slug>[-\w]+)/$', 
            ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                    'delete': 'destroy'})),
]

