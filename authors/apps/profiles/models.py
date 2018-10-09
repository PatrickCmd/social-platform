from django.db import models

from authors.apps.authentication.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profiles",
                                on_delete="models.CASCADE")
    bio = models.TextField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    following = models.BooleanField(default=False)
    users_followed = models.IntegerField(default=0)
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
