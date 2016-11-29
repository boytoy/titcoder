# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from CourseApp import models as Course
from ckeditor.fields import RichTextField

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('分类', max_length=256)
    intro = RichTextField('分类介绍', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural = '分类管理'
        ordering = ['name']

class ArticleManager(models.Manager):

	def query_by_category(self, category_id):
		query = self.get_queryset().filter(category_id=category_id)

	def query_by_user(self, user_id):
		user = Course.User.objects.get(id=user_id)
		article_list = user.article_set.all()
		return article_list

	def query_by_thumbup(self):
		query = self.get_queryset().order_by('thumbup')
		return query

	def query_by_time(self):
		query = self.get_queryset().order_by('-pub_date')
		return query

	def query_by_keyword(self, keyword):
		query = self.get_queryset().filter(title__contains=keyword)
		return query

class Author(models.Model):
    name = models.CharField('作者姓名', default='',max_length=256)
    group = models.CharField('所属群组', default='',max_length=256)
    profile = RichTextField('个人资料', default='',max_length=256)
    password = models.CharField('密码', max_length=256)
    register_date = models.DateField(verbose_name="注册日期")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者管理'
        verbose_name_plural = '作者管理'
        ordering = ['name']

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField('题目',max_length=256)
	author = models.CharField('作者',max_length=100, null=True)
	content = RichTextField('内容')
	thumbup_num = models.IntegerField(default=0,verbose_name="点赞数")
	collect_num = models.IntegerField(default=0,verbose_name="收藏数")
	comment_num = models.IntegerField(default=0,verbose_name="评论数")
	pub_date = models.DateTimeField(verbose_name="上传日期")
	update_time = models.DateTimeField(null=True,verbose_name="更新日期")
	published = models.BooleanField('上传了吗?', default=True)
	category = models.CharField('分类',max_length=100, null=True)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = '上传说明'

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章管理'
		verbose_name_plural = '文章管理'

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = '最近上传的?'

	objects = ArticleManager()

@python_2_unicode_compatible
class Comment(models.Model):
    user = models.ForeignKey(Course.User, verbose_name="评论用户", related_name="comment_user", null=True)
    article = models.ForeignKey(Article, null=True, verbose_name="评论文章")
    author = models.ForeignKey(Author, null=True, verbose_name="文章作者")
    content = RichTextField(verbose_name="评论内容")
    comment_date = models.DateField(null=True,verbose_name="评论时间")
    thumbup = models.IntegerField(default=0,verbose_name="点赞数")
    collect = models.IntegerField(default=0,verbose_name="收藏数")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = '评论管理'

class ThumbUp(models.Model):
	user = models.ForeignKey(Course.User, verbose_name="点赞用户", related_name="thumbup_user", null=True)
	article = models.ForeignKey(Article, null=True, verbose_name="点赞文章")
	comment = models.ForeignKey(Comment, related_name="thumbup_comment", verbose_name="点赞评论", null=True)
