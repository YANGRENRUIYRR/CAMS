from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
def registerview(request):
    if not request.user.is_anonymous:
        raise Http404
    return render(request,'registration/registerview.html')
def register(request,mode):
    if not request.user.is_anonymous:
        raise Http404
    if mode not in ['teacher','student']:
        raise Http404
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            if mode=='teacher':
                new_user.is_superuser=True
            new_user.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('main:index')

    # Display a blank or invalid form.
    context = {'form': form,'mode': mode}
    return render(request, 'registration/register.html', context)
@login_required
def change_password(request):
    if request.method == 'POST':
        # 创建 PasswordChangeForm 实例，并传入当前用户和 POST 数据
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # 保存用户修改后的密码
            user = form.save()
            # 更新会话中的认证哈希，防止用户修改密码后被自动登出
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('main:index')  # 重定向到主页，可根据实际情况修改
        else:
            messages.error(request, '请更正以下错误')
    else:
        # GET 请求时，创建一个空的 PasswordChangeForm 实例
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/change_password.html', {'form': form})