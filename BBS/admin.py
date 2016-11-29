from django.contrib import admin
from .models import  Article, Category, UserProfile, UserGroup, ThumbUp, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_comment', 'comment', 'date')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'hidden', 'publish_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ThumbUp)
admin.site.register(UserProfile)
admin.site.register(UserGroup)
