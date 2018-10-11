from django.urls import path, re_path

from .views import ProfileViewSet

app_name = 'profiles'
urlpatterns = [
    re_path(r'profiles/(?P<username>[-\w]+)/$', 
            ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
            name='reset-password')
]
