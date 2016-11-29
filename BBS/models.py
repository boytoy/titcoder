# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Article(models.Model):
    title = models.CharField('标题',max_length=255,unique=True)
    head_img = models.ImageField(upload_to='uploads',verbose_name='上传图片')
    summary = models.CharField('概览',max_length=55)
    category = models.ForeignKey('Category',verbose_name='分类')
    content = RichTextField('内容')
    author = models.ForeignKey('UserProfile')
    publish_date = models.DateTimeField(auto_now=True, verbose_name='上传日期')
    hidden = models.BooleanField(default=True, verbose_name='是否隐藏')
    priority = models.IntegerField('置顶?', default=1000)

    def __str__(self):
        return '<%s>, author:%s>' % (self.title, self.author)

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'

class Comment(models.Model):
    article = models.ForeignKey('Article', verbose_name='文章')
    user = models.ForeignKey('UserProfile', verbose_name='用户')
    date = models.DateTimeField(auto_now=True, verbose_name='日期')
    comment = RichTextField(max_length=1000, verbose_name='评论')
    parent_comment = models.ForeignKey('self', verbose_name='父评论', related_name='p_comment', blank=True, null=True)

    def __str__(self):
        return '<%s, user:%s>' % (self.comment, self.user)

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = '评论管理'


class ThumbUp(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True, verbose_name='日期')

    def __str__(self):
        return '<user:%s>' % self.user

    class Meta:
        verbose_name = '点赞管理'
        verbose_name_plural = '点赞管理'


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    admin = models.ManyToManyField('UserProfile')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural = '分类信息'

class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户组管理'
        verbose_name_plural = '用户组信息'
