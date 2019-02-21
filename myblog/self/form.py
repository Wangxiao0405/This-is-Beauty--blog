from .models import Usercategory,Content,Liuyan
from django.forms import ModelForm,Form
from django.forms.widgets import TextInput,Textarea,CheckboxInput,RadioSelect,Select
from ckeditor_uploader.fields import RichTextUploadingField

from django import forms
class Cate(Form):
    name=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':"input w50"}))
class ContentModelForm(ModelForm):
    class Meta:
        model=Content
        fields=['sc','theme','title','con','s']
        widgets={
            'title':TextInput(attrs={'class':"input w50"}),
            # 'con':Textarea(attrs={'class':"input",'style':"height:450px; border:1px solid #ddd;"}), #'style':"height:450px; border:1px solid #ddd;"
            'con':RichTextUploadingField(),
            's':RadioSelect(),
            'theme':Select(),
            'sc':RadioSelect(attrs={}),

        }
class LiuyanForm(ModelForm):
    class Meta:
        model=Liuyan
        fields=['name','tel','eamil','word']
        widgets={
            'name':TextInput(attrs={'placeholder':'昵称'}),
            'tel':TextInput(attrs={'placeholder':'电话'}),
            'eamil':TextInput(attrs={'placeholder':'邮箱'}),
            'word':TextInput(attrs={'placeholder':'你不想说些什么吗?(๑╹◡╹)...'}),

        }