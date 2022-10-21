from django.urls import path, include
from . import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.artor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.moive_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_review),
]

