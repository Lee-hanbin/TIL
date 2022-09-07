from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
