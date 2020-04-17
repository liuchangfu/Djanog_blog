# _*_ coding:utf-8 _*_
from django.urls import path
from . import views
from . import views_class

app_name = 'blog'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('posts/<int:pk>/', views.detail, name='detail'),
    # path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    # path('categories/<int:pk>/', views.category, name='category'),
    # path('tags/<int:pk>/', views.tag, name='tag'),
    path('', views_class.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views_class.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views_class.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views_class.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views_class.TagView.as_view(), name='tag'),

]
