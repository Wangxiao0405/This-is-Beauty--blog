from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from self.models import Content

from django.contrib.auth import authenticate, login,logout


from util.util import *
def index(request):
    # if request.user.is_authenticated:
    name=request.user.username
    print("name:",name)
    category=Category.objects.all()
    content=Content.objects.all()
    try:
        id = User.objects.filter(username=name).first().id
        type=Info.objects.filter(u_id=id).first().type
        img = User.objects.filter(username=name).first().info.img
        isadv = Info.objects.filter(u_id=id).first().isadv
        print(img)
    except:
        type=None
        img=None
        isadv=None
    return render(request,"pingtai/shouye.html",{'name':name,'type':type,'isadv':isadv,'category':category,'content':content,'img':img})




def search(request):
    if request.method=="POST":
        name = request.user.username
        print("name:", name)
        category = Category.objects.all()
        content = Content.objects.all()
        id = User.objects.filter(username=name).first().id

        try:
            type = Info.objects.filter(u_id=id).first().type
            img = User.objects.filter(username=name).first().info.img
            isadv = Info.objects.filter(u_id=id).first().isadv
            print(img)
        except:
            type = None
            img = None
            isadv = None
        print("搜索")
        q = request.POST.get('sousuo',None)
        error_msg = ''

        if not q:
            error_msg = '请输入关键词 ！！'
            return render(request, "pingtai/shouye.html",
                          {'name': name, 'type': type, 'isadv': isadv, 'category': category, 'content': content,
                           'img': img, 'error_msg': error_msg})
        else:
            post_list = Content.objects.filter(title__icontains=q)
            print(post_list)

            return render(request, "pingtai/search.html",{'name':name,'type':type,'isadv':isadv,'category':category,'content':content,
                                                      'img':img,'error_msg': error_msg,'post_list': post_list})
    return redirect(reverse("pingtai:index"))



@auth
def admin(request):
    return render(request,"pingtai/admin.html")
def cate(request):
    cate = Category.objects.all()
    if request.method == "POST":
        type=request.POST.get('type',None)
        name = request.POST.get('name',None)
        tits = request.POST.get('tits',None)
        if type != "0":
            # 添加关键字
            if name:
                KeyWord.objects.create(name=name,c_id=int(type))
            if tits:
                arr = tits.split(",")
                for item in arr:
                    KeyWord.objects.create(name=item,c_id=int(type))
        else:
            #添加分类
            if name:
                Category.objects.create(name=name)
            if tits:
                arr=tits.split(",")
                for item in arr:
                    Category.objects.create(name=item)
    return render(request,"pingtai/cate.html",{'cate':cate})

# 删除关键字:
@csrf_exempt
def delkeyword(request):
    message={'code':'','data':''}
    if request.method=="POST":
        kid=request.POST.get('id',None)
        if kid:
            message['code'] = "ok"
            KeyWord.objects.filter(id=kid).delete()
            return HttpResponse(json.dumps(message))

    message['code']="error"
    return HttpResponse(json.dumps(message))
# 删除分类:
@csrf_exempt
def delCate(request):
    message={'code':'','data':''}
    if request.method=="POST":
        kid=request.POST.get('id',None)
        if kid:
            message['code'] = "ok"
            Category.objects.filter(id=kid).delete()
            return HttpResponse(json.dumps(message))
    message['code']="error"
    return HttpResponse(json.dumps(message))
# 修改分类
@csrf_exempt
def editCate(request):
    message = {'code': '', 'data': ''}
    if request.method == "POST":
        kid = request.POST.get('id', None)
        name = request.POST.get('name', None)
        print(name)
        if kid and name:
            message['code'] = "ok"
            Category.objects.filter(id=kid).update(name=name)
            return HttpResponse(json.dumps(message))
    message['code'] = "error"
    return HttpResponse(json.dumps(message))
# 注册
def zhuce(request):
    if request.method=="POST":
        form=Zhuce(request.POST)
        if form.is_valid():
            print("注册")
            data=form.cleaned_data
            newuser=User.objects.create_user(username=data['username'], password=data['password'],email=data['email'])
            u_id=newuser.id
            href="http://"+request.get_host()+"/pingtai/loginEmail/"+data['username']+".html"
            from django.core.mail import send_mail
            send_mail(
                '天涯社区博客平台',
                '恭喜注册成功，点击链接 %s 进行跳转'%(href),
                '1353052193@qq.com',
                [data['email']],
                fail_silently=False,
            )
            Info.objects.create(is_email=1,img="img/omikron.png",phone="",company="",
                                job="",science="",reason="",age=0,sex=0,isadv=0,u_id=u_id,type=1,salary=0)

            return render(request, "pingtai/zhuce.html", {'form': form})
        else:
            return render(request,"pingtai/zhuce.html",{'form':form})
    else:
        form=Zhuce()
        return render(request,"pingtai/zhuce.html",{'form':form})
def loginEmail(request,user):
    User.objects.filter(username=user).update(is_email=1)
    return redirect("/pingtai/")
import datetime
# 登录
# def login(request):
#     if request.method=='GET':
#         form=Login()
#         return render(request,'pingtai/login.html',{'form':form})
#     else:
#         form=Login(request.POST)
#         if form.is_valid():
#             import base64
#             # 登录
#             print("登录中")
#             data=form.cleaned_data
#             if request.user.is_authenticated:
#                 print("data",data)
#                 # 帐号和密码正确，cookie保存登录状态
#                 # 获取相应对象
#                 response=redirect(reverse('pingtai:index'))
#             else:
#                 response=redirect(reverse('pingtai:admin'))
#
#             name=json.dumps(data['name']) #解决cookie不能设置中文
#             response.set_cookie('name',name)
#             print("data['name']",data['name'])
#             return response
#         else:
#             # 失败，重新登录
#             return render(request, 'pingtai/login.html', {'form': form})
def islogin(request):
    if request.method=='GET':
        form=Login()
        print("get")
        return render(request,'pingtai/login.html',{'form':form})
    else:
        form = Login(request.POST)
        error_msg = ""
        if form.is_valid():
            form=Login(request.POST)
            print("登录啊")
            print("登录中")
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            print(username,password)
            # request.user.is_authenticated:  验证是否用户是否登录，用来限制用户登录后才能执行的某些行为，必须搭配Django的登录与登出函数
            # authenticate() 提供了用户认证，即验证用户名以及密码是否正确,一般需要username  password两个关键字参数#,如果校验通过则返回User对象，如果校验不通过返回None
            user = authenticate(request,username=username, password=password)
            print(user)
            if user is not None:
                login(request,user)
                response= redirect(reverse('pingtai:index'))
                name = json.dumps(username)  # 解决cookie不能设置中文
                # response.set_cookie('name',name)
                return response
            else:
                error_msg = "用户名或者密码填写错误"
            return render(request, 'pingtai/login.html', {'form': form,'error_msg': error_msg})
        else:
            return render(request, 'pingtai/login.html', {'form': form,'error_msg': error_msg})



# def loginout(request):
#      print("退出登录")
# #      response = json.loads(request.COOKIES.get('name', None))
# #      response.delete_cookie("name")
# #      User.objects.filter(username=response).update(type=1)
# #      return redirect(reverse("pingtai:index"))
#
#      # print(2222)
#      # return response
from django.contrib.auth import logout
# 注销登录视图函数
def loginout(request):
    # 会将存储在用户session的数据全部清空，这样避免有人用当前用户的浏览器登陆然后就可以查看当前用户的数据了
    print("登出：",logout(request))
    return redirect(reverse('pingtai:islogin'))
@authuser
def person(request):
    if request.method == 'GET':
        name = ""
        if request.user.is_authenticated:
            name = request.user.username

        # type=User.objects.filter(username=name).first().info.type
        # print("类型",type)
        # queryset+字典
        person=User.objects.filter(username=name).values('username','email',).first()
        id=User.objects.filter(username=name).first().id
        try:
            info=Info.objects.filter(u_id=id).values('type','is_email','img','phone','company','job',
                                                     'real_name','reason','science','age','salary').first()
            img = User.objects.filter(username=name).first().info.img
        except:
            info=None
            img=None
        form=Upload()
        return render(request,"pingtai/person.html",{'person':person,'form':form,'info':info,'name':name,'img':img})
@authuser
def editperson(request):
    message = {'code': '', 'data': ''}
    if request.method == "POST":
        name = request.user.username
        kid = User.objects.filter(username=name).first().id
        real_name = request.POST.get('real_name', None)
        phone = request.POST.get('phone', None)
        company = request.POST.get('company', None)
        job = request.POST.get('job', None)
        reason = request.POST.get('reason', None)
        age = request.POST.get('age', None)
        salary = request.POST.get('salary', None)
        if kid and real_name and phone and company and job and reason:
            message['code'] = "ok"
            Info.objects.filter(u_id=kid).update(real_name=real_name,phone=phone,company=company,job=job,reason=reason,age=age,salary=salary)
            return redirect("pingtai:person")
    message['code'] = "error"
    return redirect("pingtai:person")
@authuser
# # form 表单提交
# def upload(request):
#     if request.method=="POST":
#         print("zz")
#         #获取文件对象   前台传来的
#         img=request.FILES.get('img',None)
#         # print(img.name)
#         # print(dir(img))
#         # 传过来的是二进制文件 wb
#         with open("upload/%s"%(img.name),"wb") as f:
#             # chunk 确保大文件的存储不会压倒系统内存，循环一块读一块
#             for chunk in img.chunks():
#                 f.write(chunk)
#         return HttpResponse("成功")
# django form验证提交
def upload(request):
    if request.method=="POST":
        name=""
        if request.user.is_authenticated:
            name=request.user.username
            print("编辑头像",name)
        id=User.objects.filter(username=name).first().id
        obj=Info.objects.filter(u_id=id).first()
        form=Upload(request.POST,request.FILES,instance=obj)
        print(form)
        if form.is_valid():
            print(222)
            form.save()
            return redirect("pingtai:person")
    return redirect("pingtai:person")


# 开通博客
# @authuser
def kaitong(request):
    name=request.user.username
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    # 打印出所有数据，没有省略号
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    f = pd.read_csv("C:\\Users\\Hasee\\Desktop\\logistic_data.csv")
    print(f)
    del f['User ID']
    f1 = pd.get_dummies(f[['Gender']])
    print("f1", f1)
    del f1['Gender_Male']
    del f['Gender']
    f2 = pd.concat([f1, f], axis=1)
    print(f2)
    X = f2.iloc[:, 0:3]
    y = f2.iloc[:, -1]
    print(X, y)
    clf = LogisticRegression(max_iter=100000, tol=0.000001)
    clf.fit(X, y)
    w = clf.coef_
    print("w", w)
    b = clf.intercept_
    print("b", b)

    if request.method == "GET":
        form = Kaitong()
        return render(request, "pingtai/kaitong.html", {'form': form,'name':name})
    else:

        name = request.user.username
        obj = User.objects.filter(username=name).first()
        form = Kaitong(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data['u_id'] = obj.id
            sex = int(data['sex'])
            age = int(data['age'])
            salary = int(data['salary'])
            a = np.array([0, age, salary]).reshape(1, 3)
            if sex == "1":
                a[0][0] = 1
            isadv = int(clf.predict(a))
            print("广告：",isadv)
            # data 字典形式 **data=username='name',sex='',...
            # Info.objects.create(**data,isadv=isadv)
            Info.objects.filter(u_id=data['u_id']).update(real_name=data['real_name'],phone=data['phone'],
                        company=data['company'],job=data['job'],reason=data['reason'],salary=data['salary'],age=data['age'],sex=data['sex'],isadv=isadv,type=3)

            # User.objects.filter(username=name).update(type=3)
            return redirect(reverse("pingtai:index"))
        else:
            return render(request, "pingtai/kaitong.html", {'form': form,'name':name})

from django.shortcuts import render
from .form import *
from .models import Case


# Create your views here.

def fangjia(request):
    # 线性回归
    from sklearn import linear_model
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from io import StringIO

    # 读取数据
    file = pd.read_csv('C:\\Users\\Hasee\\Desktop\\sn.csv')
    print("开始：")
    f = file.dropna()  # 丢失缺失值
    print(f.isnull().sum())
    # 打印出所有数据，没有省略号
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # 处理数据是汉字的数据为数值型数据
    f1 = pd.get_dummies(f[['dist', 'floor']])
    f2 = f1.drop(['dist_fengtai', 'floor_middle'], axis=1)
    f3 = f.drop(['dist', 'floor'], axis=1)
    X = pd.concat([f2, f3[['roomnum', 'halls', 'AREA', 'subway', 'school']]], axis=1)

    p = f['price']

    # 建立线性回归模型
    reg = linear_model.LinearRegression()
    reg.fit(X, p)

    w1 = reg.coef_  # 系数
    b1 = reg.intercept_  # 截距

    # 给出待预测面积 一维数据都是12列，reshape(1,-1)是将数据处理成一行 -1交给机器处理成合适的列
    area = np.array([1, 0, 0, 0, 0, 0, 1, 3, 2, 100, 1, 1]).reshape(1, -1)

    # 根据predict方法预测的价格
    print("根据predict方法预测的价格:\n", reg.predict(area))

    form = Data(request.POST)
    res={'message':'','result':''}
    if request.method=="POST":
        if form.is_valid():
            data = form.cleaned_data
            dist=data['dist']
            floor=data['floor']
            shi=int(data['shi'])
            hall=int(data['hall'])
            area1=int(data['area'])
            subway=int(data['subway'])
            school=int(data['school'])
            print("房价数据：",dist,floor,shi,hall,hall,area1,subway,school)
            a=np.array([0,0,0,0,0,0,0,shi, hall,area1,subway,school]).reshape(1, -1)
            i=int(dist)
            j=int(floor)
            print(i)
            a[0][i-1]=1
            if j!="3":
                a[0][j+4]=1
            print("a:",a)
            price=reg.predict(a)
            price1=int(price)*area1
            price2=int(price)*area1/10000
            print("price1:",price1)
            print("price2:",price2)
            res['message']='ok'
            res['result']=price2
            print(res)
        else:
            res['message']='error'
        return HttpResponse(json.dumps(res))
            # return render(request, "pingtai/result.html",{'form': form,'price':price1})
    return render(request, 'pingtai/fangjia.html',{'form': form})
def result(request):
    return render(request,"pingtai/fangjia.html")
def user(request):
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    # 打印出所有数据，没有省略号
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    f = pd.read_csv("C:\\Users\\Hasee\\Desktop\\logistic_data.csv")
    print(f)
    del f['User ID']
    f1 = pd.get_dummies(f[['Gender']])
    print("f1", f1)
    del f1['Gender_Male']
    del f['Gender']
    f2 = pd.concat([f1, f], axis=1)
    print(f2)
    X = f2.iloc[:, 0:3]
    y = f2.iloc[:, -1]
    print(X, y)
    clf = LogisticRegression(max_iter=100000, tol=0.000001)
    clf.fit(X, y)
    w = clf.coef_
    print("w", w)
    b = clf.intercept_
    print("b", b)

    # 给出要预测的数值

    form = Info(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            sex = int(data['sex'])
            age = int(data['age'])
            salary = int(data['salary'])
            a = np.array([0, age, salary]).reshape(1, 3)
            if sex=="1":
                a[0][0]=1
            isadv=int(clf.predict(a))
            # User.objects.create(**form.cleaned_data,isadv=isadv)
            return render(request, "yuce/info.html", {'form': form})
    return render(request, 'yuce/info.html', {'form': form})
