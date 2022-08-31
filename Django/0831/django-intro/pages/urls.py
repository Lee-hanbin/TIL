from django.urls import path
from . import views

# pages's urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
]
