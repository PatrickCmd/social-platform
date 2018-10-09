from rest_framework import serializers

from .models import Profile
from authors.apps.authentication.models import User


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = (
            'username',
            'bio',
            'avatar',
            'following',
            'users_followed',
            'created_at',
            'updated_at'
        )
    
    def update(self, request, validated_data):
        
        profile = Profile.objects.filter(
            pk=request.id).update(**validated_data
        )
        profile = Profile.objects.get(pk=profile)
        user = User.objects.get(pk=profile.user.pk)
        return profile
