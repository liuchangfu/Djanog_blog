import re
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Category, Tag
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.contrib import messages
from django.db.models import Q
from loguru import logger


# Create your views here.

# 首页
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', locals())


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
    post.body = md.convert(post.body)
    # 阅读量 +1
    post.increase_views()
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    return render(request, 'blog/detail.html', locals())


# 文章归档
def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', locals())


# 文章分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', locals())


# 文章标签
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', locals())


def search(request):
    q = request.GET.get('q')
    logger.info(f'输入的查询内容为:{q}')
    if not q:
        err_msg = '请输入搜索关键词'
        messages.add_message(request, messages.ERROR, err_msg, extra_tags='danger')
        return redirect('blog:index')
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', locals())
