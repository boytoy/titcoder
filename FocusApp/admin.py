# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Article, Comment, ThumbUp, Author, Category

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class FocusAdmin(admin.ModelAdmin):
	fieldsets = [
		('文章信息', {'fields': ['title', 'author', 'content', 'category', 'published'],'classes': ['collapse']}),
		('日期信息', {'fields': ['pub_date', 'update_time'],'classes': ['collapse']}),
	]
	list_display = ('title', 'author', 'category', 'pub_date')
	list_filter = ['pub_date', 'author', 'category']
	search_fields = ['author', 'category', 'title']

class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
		('评论信息', {'fields': ['article', 'author', 'content'],'classes': ['collapse']}),
		('时间信息', {'fields': ['comment_date'],'classes': ['collapse']}),
	]
	list_display = ('article','author','comment_date', 'thumbup')
	list_filter = ['comment_date']
	search_fields = ['article']

class AuthorAdmin(admin.ModelAdmin):
	fieldsets = [
		('作者信息', {'fields': ['name', 'group', 'register_date'],'classes': ['collapse']}),
		('作者资料', {'fields': ['profile'],'classes': ['collapse']}),
	]
	list_display = ('name', 'group', 'profile')
	list_filter = ['group']
	search_fields = ['name']

class CategorytAdmin(admin.ModelAdmin):
	fieldsets = [
		('分类信息', {'fields': ['name', 'intro'],'classes': ['collapse']}),
	]
	list_display = ('name', 'intro')
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Article ,FocusAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategorytAdmin)
