#  -*- coding:utf-8 -*-

from django.shortcuts import render,redirect
from users.forms import *

def register(request):
    redirect_to = request.POST.get('next',request.GET.get('next',''))

    if request.method =='POST':
        form =RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('users/login')
    else:
        form  = RegisterForm()

        return render(request,'users/register.html',{'form':form,'next':redirect_to})










