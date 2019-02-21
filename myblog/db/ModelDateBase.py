from django.db import models
class BaseModels(models.Model):
    # id=models.AutoField(primary_key=True)
    c_time=models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    u_time=models.DateTimeField(verbose_name="更新时间",auto_now=True)
    del_id=models.BooleanField(verbose_name="是否删除",default=False)
    class Meta:
        abstract=True