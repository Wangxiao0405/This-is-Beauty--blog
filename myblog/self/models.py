from django.db import models
from db.ModelDateBase import BaseModels
# Create your models here.
from blog.models import User,Category,KeyWord
from ckeditor_uploader.fields import RichTextUploadingField



class Usercategory(models.Model):
    u=models.ForeignKey(to=User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Follow(models.Model):
    follow = models.ForeignKey(to=User, related_name="follow_user",on_delete=models.CASCADE)
    fan = models.ForeignKey(to=User, related_name="fan_user",on_delete=models.CASCADE)
    def __str__(self):
        # return "follow:{},fan:{}".format(self.follow, self.fan)
        return format(self.follow)

class Content(BaseModels):
    a=models.ForeignKey(verbose_name="作者",to=User,on_delete=models.CASCADE)
    c=models.ForeignKey(verbose_name="网站分类",to=Category,on_delete=models.CASCADE)
    k=models.ForeignKey(verbose_name="关键字",to=KeyWord,on_delete=models.CASCADE)
    sc=models.ForeignKey(verbose_name="个人分类",to=Usercategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    con=RichTextUploadingField(verbose_name='正文')  # 富文本编辑器
    theme=models.IntegerField(choices=(
        (1,"简约"),
        (2,"清新"),
        (3,"雅致"),
        (4,"唯美"),
    ),default=1)
    s=models.IntegerField(choices=(
        (1,"发布"),
        (2,"草稿")
    ),default=2)
    page_view=models.IntegerField(verbose_name="浏览量")
    class Meta:
        verbose_name = "发表文章"
        verbose_name_plural = '发表文章'
    def __str__(self):
        return self.title
class Liuyan(models.Model):
    a=models.ForeignKey(verbose_name="作者",to=User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    tel=models.IntegerField(max_length=20)
    eamil=models.EmailField(max_length=20)
    word=models.CharField(max_length=20)

