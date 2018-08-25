from django.contrib import admin

from blog.models.categories import Category
from blog.models.posts import Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'writer', 'category_name')
    list_filter = ('title', 'writer')
    search_fields = ('title', 'writer')
    ordering = ('timestamp',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)


