from django.contrib import admin
from .models import Post, Comment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'views')
    list_filter = ('author', 'pub_date', 'tags')
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'
    filter_horizontal = ('tags',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('post', 'author')
    search_fields = ('content',)
