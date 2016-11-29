# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from ckeditor.fields import RichTextField

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


@python_2_unicode_compatible
class User(models.Model):
    nickname = models.CharField('昵称', default='', max_length=256)
    username = models.CharField('用户名称', default='', max_length=256)
    password = models.CharField('密码', default='', max_length=256)
    usergroup = models.CharField('用户组', default='',max_length=256)
    profile = models.TextField('个人资料', default='',max_length=256)
    register_date = models.DateField(verbose_name="注册日期")


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
        ordering = ['username']

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField('分类名', max_length=256)
	intro = models.TextField('类介绍', default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '课程分类'
		verbose_name_plural = '课程分类'
		ordering = ['name']

class CourseManager(models.Manager):

	def query_by_category(self, category_id):
		query = self.get_queryset().filter(category_id=category_id)

	def query_by_user(self, user_id):
		user = User.objects.get(id=user_id)
		course_list = user.course_set.all()
		return course_list

	def query_by_time(self):
		query = self.get_queryset().order_by('pub_date')
		return query

	def query_by_keyword(self, keyword):
		query = self.get_queryset().filter(title__contains=keyword)
		return query

	def query_by_thumbup(self, thumbup_num):
		query = self.get_queryset().order_by('thumbup')
		return query

@python_2_unicode_compatible
class Course(models.Model):
	course_id = models.IntegerField(verbose_name="课程ID",default=0)
	name = models.CharField(verbose_name="课程名",max_length=50)
	img = models.ImageField(verbose_name="课程封面",upload_to='CourseApp/static/images/courseimg/courseid', null=True)
	# course page needs start
	intro = RichTextField(verbose_name="介绍", null=True, default='')
	board = RichTextField(verbose_name="公告板", null=True, default='')
	arrange = RichTextField(verbose_name="安排", null=True, default='')
	lecture = models.FileField(verbose_name="讲义", null=True,upload_to='CourseApp/static/cimg/courseid', default='')
	vedio = models.FileField(verbose_name="视频", null=True,upload_to='CourseApp/static/cvedio/courseid', default='')
	homework = models.FileField(verbose_name="作业", null=True,upload_to='CourseApp/static/chomework/courseid', default='')
	description = RichTextField(verbose_name="说明", null=True, default='')
	# course page needs end
	author = models.ForeignKey('Author', verbose_name="作者", default='')
	thumbup_num = models.IntegerField(verbose_name="点赞数",default=0)
	collect_num = models.IntegerField(verbose_name="收藏数",default=0)
	pub_date = models.DateField(verbose_name="上传日期")
	update_time = models.DateField(verbose_name="更新日期",null=True)
	dead_line = models.DateField(verbose_name="结束日期",)
	published = models.BooleanField(verbose_name="是否上传了？", default=True)
	category = models.ForeignKey(Category, blank=True, null=True, verbose_name="课程类别")
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = '最近上传的吗？'

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '课程管理'
		verbose_name_plural = '课程管理'

	objects = CourseManager()

@python_2_unicode_compatible
class Comment(models.Model):
	user = models.ForeignKey('User', verbose_name="评论用户", null=True)
	course = models.ForeignKey('Course', verbose_name="评论用户", null=True)
	content = models.TextField(verbose_name="评论内容")
	comment_date = models.DateTimeField(verbose_name="评论时间")
	thumbup_num = models.IntegerField(default=0, verbose_name="点赞数")

	def __str__(self):
		return self.content

	class Meta:
		verbose_name = '评论管理'
		verbose_name_plural = '评论管理'

class Author(models.Model):
	name = models.CharField('作者姓名', default='',max_length=256)
	group = models.CharField('所属群组', default='',max_length=256)
	profile = models.TextField('个人资料', default='',max_length=256)
	password = models.CharField('密码', max_length=256, default='')
	register_date = models.DateField(verbose_name='注册日期')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '作者管理'
		verbose_name_plural = '作者管理'

class ThumbUp(models.Model):
	user = models.ForeignKey(User, verbose_name="点赞用户", null=True)
	course = models.ForeignKey(Course, verbose_name="点赞课程", null=True)
	comment = models.ForeignKey(Comment, verbose_name="点赞评论评论", null=True)

	class Meta:
		verbose_name = '评论管理'
		verbose_name_plural = '评论管理'
