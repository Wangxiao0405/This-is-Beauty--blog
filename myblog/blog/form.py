from django.forms import ModelForm,Form
from .models import *
from django.forms import PasswordInput,CharField,TextInput,Select,RadioSelect
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
# 注册
class Zhuce(ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={
            'password':PasswordInput()
        }
# 登录
class Login(Form):
    username=CharField()
    password=CharField(widget=PasswordInput())
    captcha=CaptchaField()

    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'password':PasswordInput()
        }
        labels = {
                    'username':"用户名",
                    'password':"请输入密码",
                    'captcha':"请输入验证码"
                }
    # def clean(self):
    #     cleaned_data=super().clean()
    #     print("我自己的验证钩子",cleaned_data)
    #     username =cleaned_data.get('name',None)
    #     password=cleaned_data.get('password',None)
    #     print(username,password)
    #     if username and password:
    #         userobj=User.objects.filter(username=username).first()
    #         if userobj:
    #             if userobj.password!=password:
    #                 raise ValidationError("密码填写错误")
    #         else:
    #             raise ValidationError("没有此用户")
# class Login(ModelForm):
#     # name=CharField()
#     # password=CharField(widget=PasswordInput())
#     captcha=CaptchaField()
#
#     class Meta:
#         model=User
#         fields=['username','password',]
#         widgets={
#             'username':TextInput(),
#             'password':PasswordInput(),
#             'captcha':CaptchaField()
#         }
#         labels={
#             'captcha':"请输入验证码"
#         }

class Upload(ModelForm):
    class Meta:
        model=Info
        fields=['img']

class Data(ModelForm):
    class Meta:
        model=Case
        fields=['dist','area','shi','hall','floor','school','subway']
        widgets={
            'area':TextInput(),
            'dist':Select(),
            'shi': TextInput(),
            'hall': TextInput(),
            'floor': Select(),
            'shool': RadioSelect(),
            'subway':Select(),
        }
class Kaitong(ModelForm):
    class Meta:
        model=Info
        fields=['phone','company','job','science','reason','real_name','age','sex','salary']
        widgets={
            'real_name': TextInput(),
            'sex': Select(),
            'age': TextInput(),
            'salary': TextInput(),
            'phone': TextInput(),
            'company':TextInput(),
            'job':TextInput(),
            'science':TextInput(),
            'reason':TextInput(),
        }
        labels = {
            'phone':"手机号",
            'company':"公司",
            'job':"职位",
            'science':'关心技术',
            'reason':'开通原因',
            'real_name':'真实姓名',
            'sex':'性别',
            'age': '年龄',
            'salary': '薪水',

        }