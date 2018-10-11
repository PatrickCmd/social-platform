from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import (ArticleViewSet, CategoryViewSet,
                    TagViewSet)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='articles')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'tags', TagViewSet, base_name='tags')


app_name = 'articles'
urlpatterns = router.urls

# urlpatterns = [
#     path('articles/', ArticleViewSet.as_view({'get': 'list', 'post': 'create'}),
#          name='article-list'),
#     re_path(r'articles/(?P<slug>[-\w]+)/$', 
#             ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                     'delete': 'destroy'}),
#             name='article-detail'),
#     path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}),
#          name='category-list'),
#     re_path(r'categories/(?P<slug>[-\w]+)/$', 
#             CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                     'delete': 'destroy'}),
#             name='category-detail'),
#     re_path(r'categories/(?P<slug>[-\w]+)/articles/$', 
#             CategoryViewSet.as_view({'get': 'retrieve'}),
#             name='category-articles'),
#     # path('categorys/', include(router.urls)),
# ]


