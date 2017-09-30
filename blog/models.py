# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '后台用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name



# 分类
#class Category(models.Model):
 #   name = models.CharField(max_length=30, verbose_name='分类名称')
 #   index = models.IntegerField(default=999,verbose_name='分类的排序')

  #  class Meta:
   #     verbose_name = '分类'
    #    verbose_name_plural = verbose_name
    #    ordering = ['index', 'id']

   # def __unicode__(self):
       # return self.name

# 自定义一个文章Model的管理器
# 1、新加一个数据处理的方法
# 2、改变原有的queryset
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=150, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
   # images_url = models.ImageField(upload_to='article/%Y/%m', verbose_name='选择图片')
    image = models.ImageField(upload_to='article/%Y/%m', null=True,blank=True, verbose_name='选择图片')
    #click_count = models.IntegerField(default=0, verbose_name='点击次数')
    read_num = models.IntegerField(default=0, verbose_name='浏览数目')#,blank=True, null=0)
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
   # category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title


class Read(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
   # desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
  #  image_s = models.ImageField(upload_to='read/%Y/%m', null=True, verbose_name='选择图片')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')


    class Meta:
        verbose_name = '站长推荐'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id','-date_publish']


    def __unicode__(self):
        return self.title



# 评论模型

#class Comment(models.Model):
 #   content = models.TextField(verbose_name='评论内容')
  #  username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
   # email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    #url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    #date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    #user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    #article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    #pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

   # class Meta:
    #    verbose_name = '评论'
     #   verbose_name_plural = verbose_name

   # def __unicode__(self):
       # return str(self.id)

# 友情链接
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
   # description = models.CharField(max_length=200, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

# 广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    description = models.CharField(max_length=200,  verbose_name='广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

SEX_CHOICES=(
    ('male','男'),
    ('female','女')
)

class user_x(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    sex = models.CharField(max_length=10,choices=SEX_CHOICES,null=True,blank=True)
    #phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField()

    class Meta:
        verbose_name = u'注册用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.username


class message(models.Model):
    users = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = u'留言'
        ordering = ['-datetime']

