"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
import myapp.views

# path('/foo', myapp.views.count)
# 우리주소/foo 가 들어왔을 때 myapp안에 있는 views의 count 함수를 실행시켜라
# name은 url의 이름 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='hello_world'),
    path('test/', myapp.views.test)
]

# http://127.0.0.1:8000/ 우리 프로젝트의 주소