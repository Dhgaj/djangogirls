# from django.db import models

# # Create your models here.


from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # 设置发布日期为当前时间
        self.published_date = timezone.now()
        # 保存修改
        self.save()

    def __str__(self):
        # 返回对象的标题
        return self.title
