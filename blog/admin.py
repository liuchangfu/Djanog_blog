from django.contrib import admin
from blog.models import Post, Category, Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)

admin.site.site_header = '博客后台管理'
admin.site.site_title = '博客管理'
