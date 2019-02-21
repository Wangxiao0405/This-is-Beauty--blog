from django.contrib import admin
from .models import Content
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    model = Content  # 模型
# Register your models here.
