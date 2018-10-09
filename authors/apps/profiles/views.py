from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import (RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.exceptions import (ValidationError,
                                       NotFound, 
                                       PermissionDenied)

from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet,
                     RetrieveModelMixin,
                     UpdateModelMixin):
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def get_object(self):
        if self.kwargs.get("username"):
            try:
                user_profile = Profile.objects.get(
                    user__username=self.kwargs["username"])
            except Profile.DoesNotExist:
                raise NotFound(
                    f"Profile for {self.kwargs.get('username')} does not exist")
            return user_profile
    
    def update(self, request, *args, **kwargs):
        if not request.user.username == kwargs.get("username"):
            raise PermissionDenied(
                "You are not allowed to perform this action on this profile")
        return super().update(request, *args, **kwargs)
