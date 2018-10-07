from django.conf import settings
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_auth.registration .views import SocialLoginView, SocialConnectView
from rest_auth.social_serializers import TwitterLoginSerializer, TwitterConnectSerializer
from rest_auth.registration.serializers import (VerifyEmailSerializer)
from allauth.account.adapter import get_adapter
from allauth.account.views import ConfirmEmailView
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from allauth.socialaccount import signals
from allauth.socialaccount.adapter import get_adapter as get_social_adapter
from allauth.socialaccount.models import SocialAccount

from rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from rest_auth.models import TokenModel

from .models import User
from .renderers import UserJSONRenderer
from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer
)


class RegistrationAPIView(CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer
    token_model = TokenModel

    # def post(self, request):
    #     user = request.data

    #     # The create serializer, validate serializer, save serializer pattern
    #     # below is common and you will see it a lot throughout this course and
    #     # your own work later on. Get familiar with it.
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(request, user)
    #     # serializer.save()
    #     token = User.objects.get(email=user['email']).token
    #     new_serializer = {"token": token}
    #     new_serializer.update(serializer.data)

    #     return Response(new_serializer, status=status.HTTP_201_CREATED)
    
    # @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegistrationAPIView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {
                "user": user,
                "token": self.token,
                "detail": "Verification e-mail sent."
            }

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }
            return data # JWTSerializer(data).data
        else:
            return TokenSerializer(user.auth_token).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        request.data.pop("password")

        return Response(self.get_response_data(request.data),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request, self.request.data)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = User.objects.get(email=self.request.data['email']).token  # jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
        return user


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class FacebookLogin(SocialLoginView):
    permission_classes = (AllowAny,)
    adapter_class = FacebookOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    permission_classes = (AllowAny,)
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter
