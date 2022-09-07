from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from .models import User      # 이렇게 직접 참조 권장 X
from django.contrib.auth.forms import UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        # model = User        # 이렇게 직접 참조 권장 X
        model = get_user_model()    # 이렇게 간접 참조 권장
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
