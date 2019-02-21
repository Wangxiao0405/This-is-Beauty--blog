from django.contrib import admin
from .models import KeyWord,Category,User,Info
from django.utils.html import mark_safe
class KeyWordInlin(admin.StackedInline):   #一对多
    model = KeyWord   #模型
    extra = 5           #数量
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def keyword(self,Cate):
        string=""
        for item in Cate.keyword_set.all():
            string+="<span style='margin-right:10px;border:1px solid red;padding:3px;box-sizing:border-box; '>%s</span>"%(item.name)
        return mark_safe(string)  #解析html标签
    inlines = [
        KeyWordInlin
    ]
    list_display = [
        "name","keyword"
    ]
admin.AdminSite.site_header=("天涯社区后台管理页面")
admin.AdminSite.site_title=("天涯社区")
admin.AdminSite.index_title=("")


def is_email_true(modeladmin, request, queryset):
    queryset.update(is_email=True)
is_email_true.short_description="邮箱验证通过"
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    model = Info  # 模型
    # fields = []     #设置展示谁
    exclude = ['isadv']  #排除展示谁
    list_display = ['u','img',"real_name","age","sex","job","company","salary","science","reason","is_email","isadv"] #列表显示
    actions = [
        is_email_true
    ]
    search_fields = ['job',"company"]
    empty_value_display = '-empty-'  #此属性会覆盖记录的空字段（None空字符串等）的默认显示值。默认值为-（破折号）
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    # actions_on_bottom = True
    # fk_fields 设置显示外键字段
    fk_fields = ('u',)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     model=User
#     list_display = [
#         "username",
#     ]