from django.urls import path, re_path

from .views import ProfileViewSet

urlpatterns = [
    re_path(r'profiles/(?P<username>[-\w]+)/$', 
            ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'}))
]
