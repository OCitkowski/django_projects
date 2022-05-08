from django.contrib import admin
from .models import Teg, Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'date_added', 'date_added', 'date_update', 'is_published')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Teg)

admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
