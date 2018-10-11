from django.db import models

from taggit.managers import TaggableManager

from authors.apps.authentication.models import User
from .utils import unique_slug


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=200, unique=True,
        help_text='Slug will be generated from the name of the category')
    author = models.ForeignKey(User, related_name="categories",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = unique_slug(self)
        return super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    author = models.ForeignKey(User, related_name="author_articles",
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Slug will be generated from the title of the article')
    description = models.TextField()
    body = models.TextField()
    image = models.URLField(
        default="https://www.planwallpaper.com/static/images/nature_backgrounds_amazing_background_cover_7052.jpg")
    category = models.ForeignKey(Category, related_name="articles",
                                 on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    class Meta:

        ordering = ['-created_at']

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = unique_slug(self)
        return super(Article, self).save(*args, **kwargs)
   