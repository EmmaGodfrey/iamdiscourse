from .models import Resource
from django.contrib import admin
from .models import Ebook, BlogPost, Resource


@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'pdf_file', 'audio_file')
    search_fields = ('title', 'author')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'url', 'file')
