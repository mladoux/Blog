from django.contrib import admin
from app.blog.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
        'updated_on',
        'publish_on'
    )
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)