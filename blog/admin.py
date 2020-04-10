from django.contrib import admin
from blog.models import Post, Category, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# 注册数据表后，后台可以添加
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# 修改头部信息和标题信
admin.site.site_header = '博客后台管理'
admin.site.site_title = '博客管理'
