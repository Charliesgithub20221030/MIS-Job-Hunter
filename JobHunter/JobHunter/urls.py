"""JobHunter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views as main_views
from login import views as login_views
from signup import views as signup_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 主頁面 
    path('main/', main_views.index),

    # 關於我們
    path('main/about/', main_views.about),

    # 加入我們
    path('main/joinus/', main_views.joinus),

    # 所有工作
    path('main/jobs/<int:page>/', main_views.jobs),

    # 登入 - 會員/企業 , 登入預設導向會員註冊
    path('login/', login_views.member_login),
    path('login/member/', login_views.member_login),
    path('login/company/', login_views.company_login),

    # 註冊 - 會員/企業 , 註冊預設導向會員註冊
    path('signup/', signup_views.member_signup),
    path('signup/member/', signup_views.member_signup),
    path('signup/company/', signup_views.company_signup),


]
