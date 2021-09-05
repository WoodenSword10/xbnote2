from django.db import models

# Create your models here.

class User_info(models.Model):
    username = models.CharField('昵称', max_length=10, blank=False, unique=True)
    password = models.CharField('密码', max_length=32, blank=False)
    age = models.IntegerField('年龄', default=0)
    sex = models.BooleanField('性别', default=False)
    created_time = models.DateField('创建时间', auto_now_add=True)
    updated_time = models.DateField('更新时间', auto_now=True)
    email = models.EmailField('邮箱', default='x@x')
    info = models.CharField('个人介绍', max_length=500, default='')
    img = models.ImageField('头像', upload_to='picture', default='')

    class Meta:
        db_table = 'User_info'
        verbose_name = '个人资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户'+self.username
