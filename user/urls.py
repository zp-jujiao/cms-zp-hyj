from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    path('detail/',views.detail),
    path('subpage/',views.subpage),
    path('subajax/',views.subajax),
]