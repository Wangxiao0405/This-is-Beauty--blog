from django.urls import path
from . import views
app_name="pingtai"
urlpatterns = [
    path('',views.index,name="index"),
    # path('admin/',views.admin,name="admin"),#后台界面
    # path('cate/',views.cate),
    # path('delkeyword/',views.delkeyword), #删除关键字
    # path('delCate/',views.delCate), #删除关键字
    # path('editCate/',views.editCate), #修改分类
    path('zhuce/',views.zhuce,name="zhuce"), #注册
    path('loginEmail/<user>.html',views.loginEmail), #修改分类
    path('islogin/',views.islogin,name="islogin"), #登录
    path('loginout/',views.loginout,name="loginout"), #退出
    path('person/',views.person,name="person"), #个人主页
    path('editperson/',views.editperson,name="editperson"), #个人主页
    path('upload/',views.upload,name="upload"), #上传头像
    path('kaitong/',views.kaitong,name="kaitong"), #开通博客
    path('fangjia/',views.fangjia,name="fangjia"),
    path('result/',views.index,name="result"),
    path('user/',views.user,name="user"), # 逻辑回归
    path('search/',views.search,name="search"), # 搜索功能

]