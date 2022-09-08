# from logging.config import _RootLoggerConfiguration
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request):
    ###################이미 로그인 되어 있으면 index로 가!#####################
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            ############# 단축평가 #############
            # next가 있으면 next로 가고 아니면 index로 가줘
            return redirect(request.GET.get_user('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    #로그아웃
    auth_logout(request)
    return redirect('articles:index')

# Create와 유사
def signup(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)   # UserCreationForm은 모델 폼임
        form = CustomUserCreationForm(request.POST)   
        if form.is_valid():                     # 근데 우리는 폼을 커스텀 했음
            # form.save()                         # 따라서 못 써
            # 회원가입 후, 로그인
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context ={
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()               # 탈퇴 후,
    auth_logout(request.user)           # 로그아웃
    return redirect('articles:index')

def update(request):
    if request.method == "POST":
        form =CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)