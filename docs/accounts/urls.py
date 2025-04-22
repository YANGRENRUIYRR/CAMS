"""Defines URL patterns for accounts."""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import redirect
from django.http import Http404
def login_not_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        # 检查用户是否已经登录
        if request.user.is_authenticated:
            # 如果用户已经登录，重定向到主页（这里假设主页的 URL 名称是 'home'）
            raise(Http404)
        else:
            # 如果用户未登录，正常调用被装饰的视图函数
            return view_func(request, *args, **kwargs)
    return wrapper_func
app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    path('login/', login_not_required(auth_views.LoginView.as_view(template_name='registration/login.html',redirect_field_name='next')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Registration page.
    path('register/', views.registerview, name='register'),
    path('register/<str:mode>', views.register,name="reg"),
    path('change_password/', views.change_password, name='change_password'),
]