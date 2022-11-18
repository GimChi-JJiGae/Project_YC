from django.urls import path
from movies import views


urlpatterns = [
    path('', views.home),
    path('<int:movie_pk>/', views.movie_detail),
    path('comments/', views.movie_comment_list),
    path('comments/<int:comment_pk>/', views.movie_comment_detail),
    path('<int:movie_pk>/comments/', views.movie_comment_create),
]