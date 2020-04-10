from django.contrib import admin
from blog.models import Post, Category, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    """
    下面的方法接收四个参数，其中前两个，一个是 request，即此次的 HTTP 请求对象，第二个是 obj，
    即此次创建的关联对象的实例，于是通过复写此方法，就可以将 request.user 关联到创建的 Post 实例上，然后将 Post 数据再保存到数据库
    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# 注册数据表后，后台可以添加
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# 修改头部信息和标题信
admin.site.site_header = '博客后台管理'
admin.site.site_title = '博客管理'
