from django.contrib import admin
from posts.models import Posts, Category


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'category', 'pub_date', 'update_date'
    )
    search_fields = (
        'id', 'title', 'author'
    )
    list_filter = (
        'title', 'author', 'category','pub_date', 'update_date'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug'
    )
    search_fields = (
        'id', 'slug'
    )
    list_filter = (
        'slug',
    )
    prepopulated_fields = {'slug': ('title',)}
