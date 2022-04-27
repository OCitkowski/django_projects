from django.contrib import admin
from .models import CommentsNote, StarsNote, CategoryNote, Note
# Register your models here.

admin.site.register(CommentsNote)
admin.site.register(CategoryNote)
admin.site.register(StarsNote)
admin.site.register(Note)


