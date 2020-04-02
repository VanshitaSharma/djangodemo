from django.contrib import admin
from .models import blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('title','id')
    list_filter=('title',)
    search_fields=('id','title')
admin.site.register(blog, BlogAdmin)
