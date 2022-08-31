from django.urls import path
from . import views

# articles's urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dtl/', views.dtl, name='dtl'),
    path('dtl2/', views.dtl2, name='dtl2'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # name이라는 변수가 str이 아니면 막아 
    path('hello/<str:name>/', views.hello, name='hello'),     
]
