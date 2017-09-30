# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import Q
from models import user_x
import re
from models import *
from crispy_forms.helper import FormHelper
from threadedcomments.forms import ThreadedCommentForm as base_class

from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate



def validate_username(value):
    if value =='username':
       raise ValidationError(u'%s is private,dont input'%value)

def validate_phone(value):
    if not value.isdigit():
        raise ValidationError(U'%S不是电话号码'%value)



SEX_CHOICES=(
('male','男'),
('female','女')
)

class LoginForm(forms.Form):
    '''
    登录Form
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={" class":"form-control","id":"usernameid" ,"placeholder": "用户名", }),
                              max_length=50,error_messages={"required": "请输入用户名",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={" class":"form-control","id":"passwordid" ,"placeholder": "密码", }),
                              max_length=20,error_messages={"required": "请输入密码",})

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            try:
                member = user_x.objects.get(username__exact=username)
            except user_x.DoesNotExist:
                self._errors['username'] = self.error_class([u'用户不存在'])
                return
            if member.password != password:
                self._errors['password'] = self.error_class([u'密码错误'])
        return cleaned_data


class RegForm(forms.Form):
    '''
    注册表单
    '''
    firstname = forms.CharField(widget=forms.TextInput(attrs={" class":"form-control","id":"firstnameid" ,"placeholder": "姓氏", }),
                              max_length=10,error_messages={"required": "姓氏不能为空",})

    lastname = forms.CharField(widget=forms.TextInput(attrs={" class":"form-control","id":"lastnameid" ,"placeholder": "名字", }),
                              max_length=10,error_messages={"required": "名字不能为空",})

    username = forms.CharField(widget=forms.TextInput(attrs={" class":"form-control","id":"usernameid" ,"placeholder": "用户名", }),
                              max_length=50,error_messages={"required": "用户名不能为空",},validators=[validate_username])

    email = forms.EmailField(widget=forms.TextInput(attrs={" class":"form-control","id":"emailid" ,"placeholder": "邮箱", }),
                              max_length=50,error_messages={"required": "邮箱不能为空",})


    password = forms.CharField(widget=forms.PasswordInput(attrs={" class":"form-control","id":"passwordid" ,"placeholder": "密码", }),
                              max_length=20,error_messages={"required": "密码不能为空",})

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={" class": "form-control", "id": "password1id", "placeholder": "再次输入密码", }),
                               max_length=20, error_messages={"required": "密码不能为空", })

    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES, error_messages={"required": "请选择性别", })

    phone = forms.CharField(required=False,validators=[validate_phone])

    class Meta:
        model = user_x
        fields = '__all__'

    def clean(self):
        cleaned_data = super(RegForm,self).clean()
        email = cleaned_data.get('email')
        db_email = user_x.objects.filter(email=email)
        username = cleaned_data.get('username')
        db_username = user_x.objects.filter(username = username)
        password = cleaned_data.get('password')
        password1 = cleaned_data.get('password1')
        if email in [email.email for email in db_email]:
            self._errors['email'] = self.error_class([u'邮箱以存在，请换一个'])
        elif username in [username.username for username in db_username]:
            self._errors['username'] = self.error_class([u'用户名以存在，请换一个or返回登录'])
        elif password != password1:
            self._errors['password1'] = self.error_class([u'输入密码不一致'])
        else:
            return cleaned_data



class ChangepwdForm(forms.Form):
    '''
    修改密码
    '''

    password = forms.CharField(widget=forms.PasswordInput(attrs={" class":"form-control","id":"oldpasswordid" ,'placeholder':'原密码'}),
                                  error_messages = {'required':'请输入原密码',})

    newpassword = forms.CharField(widget=forms.PasswordInput(attrs={" class":"form-control","id":"newpasswordid" ,'placeholder':'新密码'}),
                                  error_messages= {'required':'请输入新密码',})

    newpassword1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"newpasswordid1",'placeholder':'确认密码',}),
                                   error_messages={'required':'再次输入新密码'})


    def clean(self):
        cleaned_data = super(ChangepwdForm,self).clean()
        password = cleaned_data.get('password')
        newpassword = cleaned_data.get('newpassword')
        newpassword1 = cleaned_data.get('newpassword1')
        if newpassword != newpassword1:
            self._errors['newpassword1'] = self.error_class([u'输入密码不一致'])
        return cleaned_data

  #  def clean(self):
   #     cleaned_data = super(ChangepwdForm,self).clean()
    #    password = cleaned_data.get('password')
     #   newpassword = cleaned_data.get('newpassword')
     #   newpassword1 = cleaned_data.get('newpassword1')

      #  if password :
       #     try:
        #        member = user_x.objects.get(password__exact=password)
         #   except user_x.DoesNotExist:
          #      self._errors['password'] = self.error_class([u'原密码错误'])
           #     return
       # if newpassword != newpassword1:
        #        self._errors['newpassword1'] = self.error_class([u'输入密码不一致'])
       # return cleaned_data


















