from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect, HttpResponse
from manager.models import *
import json

# Create your views here.
list=''
newslist1=[]
contentlist=[]
def home(request):
    template=loader.get_template('user/home.html')
    global list
    list=menu.objects.values("name","id").all()
    context = {"menulist":list,"index":0}
    return HttpResponse(template.render(context,request))

def detail(request):
    template=loader.get_template('user/detail.html')
    print(list)
    context = {}
    return HttpResponse(template.render(context,request))

def subpage(request):
    template=loader.get_template('user/subpage.html')
    context = {"menulist":list,"index":1}
    return HttpResponse(template.render(context,request))

def subajax(request):
    menuid = request.GET.get('id')
    newslist=news.objects.filter(catid=menuid).order_by('registtime')
    global contentlist
    global newslist1
    for item in newslist:
        newsdict={"id":item.id,"title":item.title,"titlecolor":item.title_font_color,"thumb":item.thumb,"num":item.num}
        newslist1.append(newsdict)
        content=news_content.objects.filter(newsid=item.id).values("content","id")
        print(content)
        for item1 in content:
            contentdict={"id":item1["id"],"content":item1["content"]}
            print(contentdict)
            contentlist.append(contentdict)
    print(contentlist)
    dic={
        "news":newslist1,
        "cont":contentlist,
    }
    userinfodata = json.dumps(dic)
    response = HttpResponse(userinfodata)
    response["Access-Control-Allow-Origin"] = "*"
    return response
