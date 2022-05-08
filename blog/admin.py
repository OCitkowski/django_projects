from django.contrib import admin
from .models import Teg, Post, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Teg)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)






