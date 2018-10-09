from django.db import models

from authors.apps.authentication.models import User
from .utils import unique_slug


class Article(models.Model):
    author = models.ForeignKey(User, related_name="articles",
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Slug will be generated from the title of the post')
    description = models.TextField()
    body = models.TextField()
    image = models.URLField(
        default="https://www.planwallpaper.com/static/images/nature_backgrounds_amazing_background_cover_7052.jpg")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_at']

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = unique_slug(self)
        return super(Article, self).save(*args, **kwargs)
   