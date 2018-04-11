from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mysite.models import User
class UserAdmin(admin.ModelAdmin):
    list_filter = ['username']
    search_fields = ['username']  # 添加快速查询栏

admin.site.register(User, UserAdmin)