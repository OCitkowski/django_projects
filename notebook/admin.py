from django.contrib import admin
from .models import CommentsNote, StarsNote, CategoryNote, Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    fields = (('name' , 'url', 'stars'), 'category', 'image')
    list_display = ('name', 'text')


admin.site.register(CommentsNote)
admin.site.register(CategoryNote)
admin.site.register(StarsNote)
admin.site.register(Note, NoteAdmin)


