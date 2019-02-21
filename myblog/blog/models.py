from django.db import models
from db.ModelDateBase import BaseModels
from django.contrib.auth.models import User


from django.contrib.auth.models import AbstractUser


class Info(models.Model):
    u=models.OneToOneField(to=User,on_delete=models.CASCADE,verbose_name="用户名")
    is_email=models.BooleanField(default=False,verbose_name="邮箱是否验证")
    img=models.ImageField(upload_to="img/",verbose_name="头像")
    phone = models.CharField(max_length=11,verbose_name="电话")
    company = models.CharField(max_length=30,verbose_name="所在公司")
    job = models.CharField(max_length=20,verbose_name="所从事的职业")
    science = models.CharField(max_length=30,verbose_name="感兴趣的方面")
    reason = models.CharField(max_length=200,verbose_name="开通博客的理由")
    real_name = models.CharField(max_length=10,verbose_name="真实姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.IntegerField(verbose_name="性别",choices=(
        (0, "男"),
        (1, "女"),
    ), default=0)
    type = models.IntegerField(verbose_name="类别", choices=(
        (1, "普通用户"),
        (2, "高级用户"),
        (3, "普通管理员"),
    ), default=0)
    salary = models.IntegerField(verbose_name="月薪")
    isadv = models.IntegerField(default=0)

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = '个人信息'

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "网站种类"
        verbose_name_plural = '网站种类'

class KeyWord(models.Model):
    c=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Case(models.Model):
    area = models.IntegerField()
    dist = models.IntegerField(choices=(
        (1, "朝阳区"),
        (2, "海淀区"),
        (3, "东城区"),
        (4, "西城区"),
        (5, "石景山"),
    ), default=1)
    shi = models.IntegerField()
    hall = models.IntegerField()
    floor = models.IntegerField(choices=(
        (1, "低层"),
        (2, "中层"),
        (3, "高层"),
    ), default=1)
    school= models.IntegerField(choices=(
        (1, "是"),
        (2, "否")
    ), default=1)
    subway = models.IntegerField(choices=(
        (1, "是"),
        (2, "否")
    ), default=2)
    price=models.IntegerField()