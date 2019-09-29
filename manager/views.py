from django.template import loader
from django.shortcuts import render, redirect, HttpResponse
from django.forms import forms
from DjangoUeditor.forms import  UEditorField


# Create your views here.
def userManage(request):
    template=loader.get_template('manager/manage-user.html')
    context = {}
    return HttpResponse(template.render(context,request))

def regist(request):
    form=TestUEditorForm()
    return render(request,"manager/manage-user.html",{"form":form})


class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="static/images/", filePath="static/files/",upload_settings={"imageMaxSize":1204000},settings={})


