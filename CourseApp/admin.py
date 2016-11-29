# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User, Comment, Author, Course, ThumbUp, Category

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class CourseAdmin(admin.ModelAdmin):
	fieldsets = [
		('课程信息', {'fields': ['course_id', 'name', 'author', 'img', 'category', 'published'],'classes': ['collapse']}),
		('课程主页', {'fields': ['intro', 'board', 'arrange', 'description'],'classes': ['collapse']}),
		('日期信息', {'fields': ['pub_date','dead_line', 'update_time'],'classes': ['collapse']}),
	]
	list_display = ('name','intro','category','pub_date')
	list_filter = ['pub_date']
	search_fields = ['course_name']

class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
		('评论信息', {'fields': ['course', 'user', 'content'],'classes': ['collapse']}),
		('日期信息', {'fields': ['comment_date'],'classes': ['collapse']}),
	]
	list_display = ('course','user','comment_date', 'thumbup_num')
	list_filter = ['comment_date']
	search_fields = ['course']

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		('用户信息', {'fields': ['nickname','username', 'password', 'usergroup'],'classes': ['collapse']}),
		('个人资料', {'fields': ['register_date','profile'],'classes': ['collapse']}),
	]
	list_display = ('username','usergroup', 'profile')
	list_filter = ['usergroup']
	search_fields = ['id', 'username']

class AuthorAdmin(admin.ModelAdmin):
	fieldsets = [
		('作者信息', {'fields': ['name', 'group', 'register_date'],'classes': ['collapse']}),
		('个人资料', {'fields': ['profile'],'classes': ['collapse']}),
	]
	list_display = ('id','name', 'group', 'profile')
	list_filter = ['group']
	search_fields = ['name']

class CategorytAdmin(admin.ModelAdmin):
	fieldsets = [
		('分类信息', {'fields': ['name', 'intro'],'classes': ['collapse']}),
	]
	list_display = ('name', 'intro')
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Course,CourseAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategorytAdmin)
