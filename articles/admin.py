from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ['title',]
    fields = ("title", "image_tag", "description", "image_url",)
    readonly_fields = ('image_tag',)

admin.site.register(Article, ArticleAdmin)
