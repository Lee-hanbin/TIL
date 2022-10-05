from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:comment_pk>/comments/delete/', views.comments_delete, name = 'comments_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name = 'comments_delete'),
    # 위에 걸로 하면 갑자기 comment가 뜬금없이 나오는 느낌! 
    # 웬만하면 아래 걸로 쓰자!
]

