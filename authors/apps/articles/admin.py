from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('author', 'category', 'title', 'slug', 'description', 'body')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('name', 'slug', 'author')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
