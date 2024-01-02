from django.contrib import admin
from home.models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'body', 'post', 'created_on','approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('email', 'body')
    action = ['approve_comment']
    
    def approve_comment(self, request, queryset):
        queryset.update(approved=True)


