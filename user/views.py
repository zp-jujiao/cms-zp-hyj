from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home(request):
    template=loader.get_template('user/home.html')
    context = {}
    return HttpResponse(template.render(context,request))

def detail(request):
    template=loader.get_template('user/detail.html')
    context = {}
    return HttpResponse(template.render(context,request))

def subpage(request):
    template=loader.get_template('user/subpage.html')
    context = {}
    return HttpResponse(template.render(context,request))