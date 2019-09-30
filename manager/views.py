from django.template import loader
from django.shortcuts import render, redirect, HttpResponse
from django.forms import forms
from DjangoUeditor.forms import  UEditorField
from manager.models import *

# Create your views here.
#管理员管理
def userManage(request):
    template=loader.get_template('manager/manage-user.html')
    context = {}
    return HttpResponse(template.render(context,request))

def regist(request):
    form=TestUEditorForm()
    return render(request,"manager/manage-user.html",{"form":form})


class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="static/images/", filePath="static/files/",upload_settings={"imageMaxSize":1204000},settings={})

# 登录页面渲染
def login(request):
    template=loader.get_template('manager/manage-login.html')
    context = {}
    return HttpResponse(template.render(context,request))

def loginHandler(request):
    # 接收前端提交的数据
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    login_list = admin.objects.values("username",).all()
    return HttpResponse(1)
