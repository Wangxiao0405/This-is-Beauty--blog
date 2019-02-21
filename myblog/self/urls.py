
from django.urls import path
from . import views
app_name="self"
urlpatterns = [
    path('index/<name>/',views.index,name="index"),  #个人博客首页
    path('liuyan/',views.liuyan,name="liuyan"),  #留言
    path('listliuyan/',views.listliuyan,name="listliuyan"),  #查看留言
    path('delliuyan/',views.delliuyan,name="delliuyan"),  #查看留言
    path('lianjie/',views.lianjie,name="lianjie"),  #链接
    path('admin/',views.admin,name="admin"),  #后台管理页面
    path('cate/',views.cate,name="cate"),  #个人博客分类
    path('delCate/',views.delCate,name="delCate"),  # 删除分类
    path('editCate/',views.editCate,name="editCate"),  # 修改分类
    path('content/',views.content,name="content"),  # 添加文章
    path('listcontent/',views.listcontent,name="listcontent"),  # 添加文章
    path('delcontent/',views.delcontent,name="delcontent"),  # 删除文章
    path('editcontent/',views.editcontent,name="editcontent"),  # 修改文章
    path('NB/<testWords>/',views.NB,name="NB"),  # 朴素贝叶斯算法
    path('detail/<id>/', views.detail, name="detail"),  # 详情
    path('follow/', views.follow, name="follow"),  # 关注
    path('quxiaofollow/', views.quxiaofollow, name="quxiaofollow"),  # 取消关注


]