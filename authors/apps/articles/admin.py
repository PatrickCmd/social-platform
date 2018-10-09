from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('author', 'title', 'slug', 'description', 'body')

admin.site.register(Article, ArticleAdmin)
