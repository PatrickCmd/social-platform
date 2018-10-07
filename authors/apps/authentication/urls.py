from django.conf.urls import url
from django.urls import path, re_path, include
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,
    FacebookLogin, FacebookConnect, TwitterLogin, TwitterConnect,
    VerifyEmailView
)


# Use the new path module in django 2.0
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view(), name='login'),
]

urlpatterns += [
    path('account-confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(),
            name='account_confirm_email'),
    re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    re_path('socialaccounts/(?P<pk>\d+)/disconnect/$',
         SocialAccountDisconnectView.as_view(),
         name='social_account_disconnect'),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]