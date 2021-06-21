from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('title', 'author', 'state', 'created', 'published')
	list_filter=('state','created','published')