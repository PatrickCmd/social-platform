"""authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from django.views import generic

from rest_framework import views, serializers, status
from rest_framework.response import Response
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


# swagger documentation
schema_swagger_view = get_swagger_view(title='Social Platform API')
# coreapi documentation
schema_view = get_schema_view(title="Social Platform API")


urlpatterns = [
    re_path(r'^$', generic.RedirectView.as_view(
        url='/api/', permanent=False
    )),
    
    # authentication urls
    path('api/', include(('authors.apps.authentication.urls', 'authentication'),
         namespace='authentication')),
    
    # admin urls
    path('admin/', admin.site.urls),

    # rest_framework urls for session authentication for the browsable api
    re_path(r'^api-auth/', include('rest_framework.urls')),
    
    # documentation urls
    path(r'api_docs', schema_swagger_view),
    path(r'docs', include_docs_urls(title='Social Platform API', permission_classes=[])),
    path(r'schema', schema_view),
]
