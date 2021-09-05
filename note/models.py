from django.db import models
from users.models import User_info
# Create your models here.
class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    classify = models.CharField('分类', max_length=10, default='')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User_info, on_delete=models.CASCADE)
    is_active = models.BooleanField('是否被删除', default=False)

    class Meta:
        db_table = 'Note'
        verbose_name = '笔记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s-%s'%(self.user.username, self.title)