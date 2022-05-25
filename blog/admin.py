from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.contrib.admin.views.main import ChangeList
from . forms import PostsChangeListForm

from .models import Tag, Post, Category, Comment

@admin.action(description='Mark selected blog as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

@admin.action(description='Mark selected blog as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')

@admin.action(description='Mark selected blog as withdrawn')
def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')


class PostChangeList(ChangeList):

    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin,
        sortable_by, search_help_text,):

        super(PostChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable,
            model_admin, sortable_by, search_help_text,)

        self.prepopulated_fields = {'slug': ('title',)}
        self.list_display = ['id','action_checkbox', 'title', 'category', 'tag', 'get_tegs', 'status',
                            'text', 'image', 'date_added', 'date_update', 'owner', ]
        self.list_editable = ['text', 'image', 'category', 'status', 'owner', 'tag']
        self.list_display_links = ['title']

        # self.filter_horizontal = ('tag',)


class PostAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft, make_withdrawn]
    prepopulated_fields = {"slug": ("title",)}

    def get_changelist(self, request, **kwargs):
        return PostChangeList

    def get_changelist_form(self, request, **kwargs):
        return PostsChangeListForm

# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('id', 'title', 'category', 'status', 'text', 'image', 'date_added', 'date_update', 'get_products', 'owner')
#     list_editable = ('text', 'image', 'category', 'status', 'owner')
#     actions = [make_published, make_draft, make_withdrawn]
#     filter_horizontal = ('tag',)


    # @admin.action(description='Mark selected stories as published')
    # def make_published(self, request, queryset):
    #     updated = queryset.update(status='p')
    #     self.message_user(request, ngettext(
    #         '%d story was successfully marked as published.',
    #         '%d stories were successfully marked as published.',
    #         updated,
    #     ) % updated, messages.SUCCESS)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
