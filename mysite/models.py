from django.db import models
# Create your models here.
# 创建模型的管理类
class UserManager(models.Manager):
    def create(self, username, password,):
        user = User()
        user.username = username
        user.password = password
        return user

# 创建自己的模型类。
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)

    # 创建元数据
    class Meta:
        ordering = ['userid']
        # 设置表名字
        db_table = 'user'

    maneger = UserManager()