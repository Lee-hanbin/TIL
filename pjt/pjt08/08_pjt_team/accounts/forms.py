from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    # UserCreationForm을 상속받아 CustomUserCreationForm을 만든다.
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 이름",
        })
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호(8자 이상)",
        })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 확인",
        })
    )
    class Meta:
        model = get_user_model() # 이 폼이 적용될 모델을 지정한다.
        fields = ['username', 'password1', 'password2',]
        # 이 폼에서 입력 받을 필드명을 지정한다.
