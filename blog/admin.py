# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title','read_num' ,'desc', )#'read_num')#'click_count',)
    list_display_links = ('title', 'desc', )
    #list_editable = ('read_num',)#('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user' ,'image','tag', )#'category'
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ( 'is_recommend','read_num')#'click_count')
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class ReadAdmin(admin.ModelAdmin):
    list_display = ('title','user',)
    list_display_links = ('title','user',)

    fieldsets = (
        (None,{
            'fields':('title','content','user','index',)
        }),

        )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


class messageadmin(admin.ModelAdmin):
    list_display = ('title','datetime','users')




admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
#admin.site.register(Category)
admin.site.register(Links)
admin.site.register(Ad)
admin.site.register(user_x)
admin.site.register(Read,ReadAdmin)
admin.site.register(message,messageadmin)
