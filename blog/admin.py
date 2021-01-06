from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_slug', 'post_created', 'status')
    list_filter = ('status',)
    search_fields = ['post_title', 'post_slug', 'post_content'],
    prepopulated_fields = {'post_slug': ('post_title',)}


admin.site.register(BlogPost, BlogAdmin)
