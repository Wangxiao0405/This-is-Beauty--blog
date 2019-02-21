import json
from blog.models import User
from django.shortcuts import redirect,reverse
from django.contrib.auth import authenticate, login,logout

# 验证是否为平台管理员的装饰器
def auth(fn):
    def newfn(request,*args,**kwargs):
        if request.user.is_authenticated:
            name = request.user.username
            quserset=User.objects.filter(username=name)
            if len(quserset)>0 and quserset[0].type==2:
                res=fn(request,*args,**kwargs)
                return res
        return redirect(reverse("pingtai:islogin"))
    return newfn
# 验证是否为用户的装饰器
def authuser(fn):
    def newfn(request,*args,**kwargs):
        if request.user.is_authenticated:
            name = request.user.username
            quserset=User.objects.filter(username=name)
            if len(quserset)>0:
                res=fn(request,*args,**kwargs)
                return res
        return redirect(reverse("pingtai:islogin"))
    return newfn