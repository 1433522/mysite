from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#网站首页
    path('category-<int:cid>.html', views.category, name='category'),#目录
    path('archive/<int:year>/<int:month>', views.archive, name='archive'),#归档页面
    path('search/', views.search, name='search'),#搜索列表页
    path('show-<int:sid>.html', views.show, name='show'),#内容页
]
