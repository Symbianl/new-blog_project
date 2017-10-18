# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render, redirect, render_to_response,HttpResponse,HttpResponseRedirect,RequestContext,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader,Context
from django.core.urlresolvers import reverse
from django.conf import settings
from django import forms
from django.contrib import auth
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Count
from models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings as django_settings
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import send_mail
from itsdangerous import URLSafeTimedSerializer as utsr
import base64
import re
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView

logger = logging.getLogger('blog.views')

# Create your views here.
def global_setting(request):
    # 站点基本信息
    SITE_URL = settings.SITE_URL
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
     # 分类信息获取（导航数据）
  #  category_list = Category.objects.all()
    #广告数据
   # ad_list = Ad.objects.all()[:5]
    # 文章归档数据
    archive_list = Article.objects.distinct_date()
    #标签云
    tag_list = Tag.objects.all()
    #友情链接
    link_list = Links.objects.all()
    #排行文章
    article_list=Article.objects.all()
    #文章排行数据
    click_article_list = article_list.order_by('-read_num')[:6]
    #站长推荐
    recommend_read_list =  Read.objects.all()[:6]

    # 评论排行
    #comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
   # article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    return locals()

@csrf_exempt
def index(request):
    try:
        # 最新文章数据
        article_list=Article.objects.all()
        article_list = getPage(request, article_list)
        username = request.session.get('username', "")

    except Exception as e:
        print e
        logger.error(e)
    return render(request,'index.html',locals())

def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        article_list = getPage(request, article_list)
        username = request.session.get('username', "")#在该模板页面中获取用户名的名字

    except Exception as e:
        logger.error(e)
    return render(request, 'archive.html', locals())

# 按标签查询对应的文章列表
def tag(request):
    username = request.session.get('username', "")
    try:
        # 先获取客户端提交的标签
        aid = request.GET.get('aid', None)
        try:
        # 注意这里tag和article是多对多关系，需要分两步取出标签下的所有文章，要用到_set
            tag = Tag.objects.get(pk=aid)
        except Tag.DoesNotExist:
            return render(request, 'failure.html', {'reason': '分类不存在'})
        article_list = Article.objects.filter(tag=tag)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger.error(e)
    return render(request, 'tag.html', locals())

# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

# 文章详情
def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
            if not request.COOKIES.has_key('article_%s_readed'%(id)):
                article.read_num+=1
                article.save()

        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})

    except Exception as e:
        print e
        logger.error(e)

    response = render(request,'article.html',{'article':article})
    response.set_cookie('article_%s_readed'%(id),'True')
    return render(request, 'article.html', locals())

    return response



def read(request):
    username = request.session.get('username', "")
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            read = Read.objects.get(pk=id)
        except Read.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})

    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'read.html', locals())


#def category(request):
 #   try:
     #   # 先获取客户端提交的信息
      #  cid = request.GET.get('cid', None)
      #  try:
       #     category = Category.objects.get(pk=cid)
      #  except Category.DoesNotExist:
      #      return render(request, 'failure.html', {'reason': '分类不存在'})
      #  article_list = Article.objects.filter(category=category)
      #  article_list = getPage(request, article_list)
   # except Exception as e:
   #     logger.error(e)
  #  return render(request, 'category.html', locals())


def message(request):
    username = request.session.get('username', "")
    return render(request,'message.html',locals())


def search(request):
    username = request.session.get('username', "")

    search = True

    error = False
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'search1.html')
        else:
            article = Article.objects.filter(title__icontains=s)
            if len(article) == 0:
                error = True


    return render_to_response('search1.html',
                              locals(),
                              context_instance=RequestContext(request))




def error(request):
    return render(request, '404.html', locals())










