from django.contrib import admin
from .models import Article,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','date','category')
    search_fields = ('title','body')
    ordering = ('-date',)
    list_display_links = ('id', 'title')
