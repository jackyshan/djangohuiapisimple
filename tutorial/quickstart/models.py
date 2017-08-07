# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    aid = models.AutoField(primary_key=True) #id
    title = models.CharField(max_length=100, blank=True, default='资讯标题') #标题
    category = models.TextField(default='行业动态') #分类
    source = models.TextField(default='H-ui') #来源
    update_time = models.TextField(default='2017-8-6') #更新时间
    see_times = models.TextField(default='1111') #浏览次数
    publish_status = models.IntegerField(default=0) #发布状态 0未发布 1已发布 2草稿

    class Meta:
        ordering = ('created',)
