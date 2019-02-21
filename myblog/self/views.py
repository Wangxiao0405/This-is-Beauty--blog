from django.shortcuts import render,HttpResponse,reverse,redirect
import json
import re
import numpy as np
import jieba
from blog.models import *
from self.models import Usercategory,Liuyan,Content,Follow
from util.util import authuser,auth
from django.core import paginator
from self.form import LiuyanForm,ContentModelForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 个人博客主页
@authuser
def index(request,name):
    name = ""
    if request.user.is_authenticated:
        name = request.user.username
        id = User.objects.filter(username=name).first().id
        imgurl = Info.objects.filter(u_id=id).first().img
        type = Info.objects.filter(u_id=id).first().type
        if type==3:
            content = Content.objects.filter(a_id=id).all()
            print(content)
            return render(request,"self/index.html",{'name': name, 'img': imgurl,'content':content})
        else:
            return redirect(reverse("pingtai:kaitong"))
# 留言
@csrf_exempt
@authuser
def liuyan(request):
    message = {'type': '', 'nicheng': '','tel':'','eamil':'','word':'','count':''}
    name = request.user.username
    id = User.objects.filter(username=name).first().id
    imgurl = Info.objects.filter(u_id=id).first().img
    form = LiuyanForm(request.POST)
    liuyan=Liuyan.objects.all()

    count=liuyan.count()
    print("123456789")
    if request.method=='POST':
        print("liuyan")
        nicheng = request.POST.get('nicheng', None)
        tel = request.POST.get('tel', None)
        eamil = request.POST.get('eamil', None)
        word = request.POST.get('word', None)
        print(tel,word)
        predict=NB(request, word)
        print("predict",predict)
        if predict==0:
            Liuyan.objects.create(name=nicheng, tel=tel, eamil=eamil, word=word, a_id=id)
            message['type']="ok"
            message['nicheng']=nicheng
            message['tel']=tel
            message['eamil']=eamil
            message['word']=word
            message['count']=count
        else:
            print("恶意评论")
            message['type']="error"
        return HttpResponse(json.dumps(message))

    return render(request, "self/liuyan.html",{'name': name, 'img': imgurl,'form':form,'liuyan':liuyan,'count':count})
# 查看留言
def listliuyan(request):
    name = request.user.username
    a_id=User.objects.filter(username=name).first().id
    liuyan=Liuyan.objects.filter(a_id=a_id).all()

    # 使用Paginator方法返回一个分页的对象，这个对象包括所有数据，分页的情况
    pag = paginator.Paginator(liuyan, 3)

    page = request.GET.get('page',1)  # QueryDict objects,如果没有对应的page键，就返回默认1。
    page_info = pag.get_page(page)  # 根据索引page，返回该page页数据，如果不存在，引起 InvalidPage异常

    # 构造上下文，以便html文件中能调用对应页的数据

    return render(request, "self/listliuyan.html",{'liuyan':liuyan,'page_info':page_info})
# 删除留言
@csrf_exempt
def delliuyan(request):
    message = {'code': '', 'data': ''}
    if request.method == "POST":
        kid = request.POST.get('id', None)
        if kid:
            message['code'] = "ok"
            Liuyan.objects.filter(id=kid).delete()
            return HttpResponse(json.dumps(message))
    message['code'] = "error"
    return HttpResponse(json.dumps(message))

# 后台管理页面
@authuser
def admin(request):
    name=request.user.username
    id = User.objects.filter(username=name).first().id
    imgurl = Info.objects.filter(u_id=id).first().img
    return render(request,"self/admin.html",{'name': name, 'img': imgurl})
def cate(request):
    cate = Usercategory.objects.all()
    if request.method=="POST":

        name = request.user.username
        u_id=User.objects.filter(username=name).first().id
        title = request.POST.get('title', None)
        print(title)
        if title:
            Usercategory.objects.create(name=title, u_id=u_id)
    return render(request, "self/cate.html",{'cate':cate})
# def cate(request):
#     name = request.COOKIES.get("name", None)
#     name = json.loads(name)
#     u_id = User.objects.filter(username=name).first().id
#     cate=Usercategory.objects.filter(u_id=u_id)
#     if request.method == "POST":
#         form=Cate(request.POST)
#         print(dir(form))
#         if form.is_valid:
#             name=form.cleaned_data['name']
#             Usercategory.objects.create(name=name, u_id=u_id)
#             return render(request, "self/cate1.html", {'form': "",'cate': cate})
#         else:
#             return render(request, "self/cate1.html", {'form':form,'cate': cate,})
#
#     else:
#         form=Cate()
#     return render(request, "self/cate1.html",{'form':form,'cate': cate})


# 删除个人博客分类:
@csrf_exempt
def delCate(request):
    message={'code':'','data':''}
    if request.method=="POST":
        kid=request.POST.get('id',None)
        if kid:
            message['code'] = "ok"
            Usercategory.objects.filter(id=kid).delete()
            return HttpResponse(json.dumps(message))
    message['code']="error"
    return HttpResponse(json.dumps(message))
# 修改个人博客分类
@csrf_exempt
def editCate(request):
    message = {'code': '', 'data': ''}
    if request.method == "POST":
        kid = request.POST.get('id', None)
        name = request.POST.get('name', None)
        print(name)
        if kid and name:
            message['code'] = "ok"
            Usercategory.objects.filter(id=kid).update(name=name)
            return HttpResponse(json.dumps(message))
    message['code'] = "error"
    return HttpResponse(json.dumps(message))


@authuser
def content(request):

    name = request.user.username
    # form=""
    cate=Category.objects.all()
    if request.method=="GET":
        form=ContentModelForm()
    else:
       # 表单提交
       # 验证modelform  关键字 分类 手动验证
       # 出错
        form = ContentModelForm(request.POST)

        if form.is_valid():
            print("验证成功")
            #手动验证
            kw=request.POST.get('kw',None)
            print("kw",kw)
            if kw:
                length=len(KeyWord.objects.filter(id=kw))
                if length>0:
                    k=KeyWord.objects.filter(id=kw).first()
                    c=k.c

                    a = User.objects.filter(username=name).first()
                    data=form.cleaned_data
                    textWords=data['con']
                    NB(request,textWords)
                    Content.objects.create(**form.cleaned_data,k=k,c=c,a=a,page_view=0)
        else:
            pass
    return render(request,"self/addcon.html",{'form':form,'cate':cate})
# 查看博客文章
@authuser
def listcontent(request):

    name = request.user.username
    a_id = User.objects.filter(username=name).first().id
    content = Content.objects.filter(a_id=a_id).all()
    pag = paginator.Paginator(content, 3)
    # 使用此判断语句是为了在用户跳转www.xxx.com/info/时也能访问第一页

    # 返回指定（page）页的数据，用于呈现在指定页上
    page = request.GET.get('page', 1)  # QueryDict objects,如果没有对应的page键，就返回默认1。
    page_info = pag.get_page(page)  # 根据索引page，返回该page数据，如果不存在，引起 InvalidPage异常
    return render(request,"self/listcon.html",{'page_info':page_info})
# 删除博客文章
# 删除个人博客分类:
@csrf_exempt
def delcontent(request):
    message={'code':'','data':''}
    if request.method=="POST":
        kid=request.POST.get('id',None)
        if kid:
            message['code'] = "ok"
            Content.objects.filter(id=kid).delete()
            return HttpResponse(json.dumps(message))
    message['code']="error"
    return HttpResponse(json.dumps(message))
# 修改博客文章
@csrf_exempt
def editcontent(request):
    name = request.user.username
    cate=Category.objects.all()
    if request.method=="GET":
        form=ContentModelForm()
    else:
       # 表单提交
       # 验证modelform  关键字 分类 手动验证
       # 出错
        form = ContentModelForm(request.POST)
        id=request.POST.get('id',None)
        print("修改的id",id)
        if form.is_valid():
            #手动验证
            kw=request.POST.get('kw',None)
            print("kw",kw)
            if kw:
                length=len(KeyWord.objects.filter(id=kw))
                if length>0:
                    k=KeyWord.objects.filter(id=kw).first()
                    c=k.c

                    a = User.objects.filter(username=name).first()
                    data=form.cleaned_data
                    textWords=data['con']
                    NB(request,textWords)
                    Content.objects.filter(id=id).update(title=data['title'],con=data['con'],theme=int(data['theme']),s=int(data['s']),sc=int(data['sc']),k=k,c=c,a=a,page_view=0)
        else:
            pass
    return render(request,"self/editcon.html",{'form':form,'cate':cate})
# 详情页
def detail(request,id):
    con=Content.objects.filter(id=id)
    fan_id=request.user.id #登录的人点击别人的关注，也就是粉丝

    name=Content.objects.filter(id=id).first().a  #每一个详情页的作者，被关注者
    name_id=User.objects.filter(username=name).first().id

    follows=Follow.objects.filter(fan_id=fan_id).all()  #登录的人的所有关注者
    is_guanzhu=""
    for item in follows:
        print(item)
        follow_id=User.objects.filter(username=item).first().id
        print(follow_id)
        if name_id==follow_id:
            is_guanzhu=1
            break
        else:
            is_guanzhu=0
    try:
        img=Content.objects.filter(id=id).first().a.info.img
    except:
        img=None
    print("zuozhe",name)
    return render(request, "self/xiangqing.html",{'name':name,'con':con,'img':img,'is_guanzhu':is_guanzhu})
# 关注
@csrf_exempt
def follow(request):
    message={'result':''}
    if request.is_ajax:
        fan=request.user.id
        guanzhu=request.POST.get('guanzhu',None)
        print("粉丝",fan)
        print("被关注者",guanzhu)
        follow=User.objects.filter(username=guanzhu).first().id
        print(follow)
        Follow.objects.create(fan_id=fan,follow_id=follow)
        message['result']="ok"
        return HttpResponse(json.dumps(message))
# 取消关注
@csrf_exempt
def quxiaofollow(request):
    message = {'result': ''}
    if request.is_ajax:
        fan = request.user.id
        guanzhu = request.POST.get('guanzhu', None)
        print("粉丝", fan)
        print("被关注者", guanzhu)
        follow = User.objects.filter(username=guanzhu).first().id
        print(follow)
        Follow.objects.filter(follow_id=follow).delete()
        message['result'] = "ok"
        return HttpResponse(json.dumps(message))
# 渲染关注页面
@authuser
def lianjie(request):
    name = request.user.username
    id = User.objects.filter(username=name).first().id
    imgurl = Info.objects.filter(u_id=id).first().img
    follows = Follow.objects.filter(fan_id=id).all()  # 登录的人的所有关注者
    for items in follows:
        try:
            follow_img=items.follow.info.img
        except:
            follow_img=None
        print(follow_img)
    return render(request, "self/lianjie.html", {'name': name, 'img': imgurl,'follows':follows})
# 朴素贝叶斯算法
def NB(request,testWords):
    print("这是朴素贝叶斯")
    import re
    import numpy as np
    import jieba

    def textParse(line):
        line = line.strip()
        line = re.sub(r'[a-zA-Z.【】0-9、。，/！…~\*\n]', '', line)
        line = jieba.lcut(line, cut_all=True)
        return [w for w in line if len(w) > 1]

    wordList = []
    classList = []
    for i in range(1, 26):
        wordList_s = textParse(
            open("C:\\Users\\Hasee\\Desktop\\人工智能\\Python课程\\机器学习\\朴素贝叶斯垃圾邮件分类\\中文版\\垃圾邮件\\%d.txt" % i,
                 encoding='UTF-8').read())
        wordList.append(wordList_s)
        classList.append(1)

        wordList_h = textParse(
            open("C:\\Users\\Hasee\\Desktop\\人工智能\\Python课程\\机器学习\\朴素贝叶斯垃圾邮件分类\\中文版\\正常邮件\\%d.txt" % i,
                 encoding='UTF-8').read())
        wordList.append(wordList_h)
        classList.append(0)

    # 构建词频
    def creatVocabList(wordList):
        vocabSet = set([])  # 去重
        for document in wordList:
            vocabSet = vocabSet | set(document)
        vocabList = list(vocabSet)
        return vocabList

    # 创建测试词集的向量  setOfWods2Vec 词级模型(出现即为1)，bagOfWods2Vec 词袋模型（出现的次数）
    def setOfWords2Vec(vocabList, words):
        wordVec = np.zeros(len(vocabList))
        for word in words:
            if word in vocabList:
                wordVec[vocabList.index(word)] = 1
        return wordVec

    vocabList = creatVocabList(wordList)
    trainMat = []
    for words in wordList:
        trainMat.append(setOfWords2Vec(vocabList, words))

    from sklearn.naive_bayes import GaussianNB, MultinomialNB
    gnb = MultinomialNB()
    model = gnb.fit(np.array(trainMat), np.array((classList)))
    # path = "C:\\Users\Hasee\\Desktop\\人工智能\\Python课程\\机器学习\\朴素贝叶斯垃圾邮件分类\\中文版\\正常邮件\\15.txt"
    # testWords = textParse(open(path, encoding="UTF-8").read())
    # testWords = ['like']
    # print(testWords)
    newWordVec = np.array(setOfWords2Vec(vocabList, testWords)).reshape(1, -1)
    print(testWords)
    result=model.predict(newWordVec)[0]
    print("朴素贝叶斯结果",result)
    return result



