from random import choices
from django import forms

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATION_CHOICES =[
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
#     #form의 widgets 사용하여 textarea 생성
#     content = forms.CharField(widget=forms.Textarea)      
#     # nation = forms.ChoiceField(choices=NATION_CHOICES)   
#     nation = forms.ChoiceField(choices=NATION_CHOICES, widget=forms.RadioSelect)   

from .models import Article

class ArticleForm(forms.ModelForm):
    title =forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the title',       # 입력창에 입력 전에 나오는 문구
                'maxlength' : 10,                        # 위젯은 유효성 검사와 무관
            }                                            # 쟝고와 상관없이 단지 10자까지만 입력되게 하는 것
        )
    )

    content = forms.CharField(
        label='내용',
        widget= forms.Textarea(
            attrs={
                'class' : 'my-content form-control' ,
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols':50,                
            }
        ),
        error_messages={
            'required' : 'Please enter your content',   # 에러 메세지 지정
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title')