from django.urls import path
from movies import views


urlpatterns = [
    path('', views.home),
    path('<int:movie_pk>/', views.movie_detail),
    path('comments/', views.movie_comment_list),
    path('<int:pk>/comments/', views.movie_detail_comments),
    path('<int:movie_pk>/comments/create/', views.movie_comment_create),
    path('<int:movie_pk>/likes/', views.likes),
    path('<int:movie_pk>/get_likes/', views.get_likes),
    path('<int:movie_comment_pk>/comments/like/', views.comment_like),
    path('<int:movie_comment_pk>/comments/hate/', views.comment_hate),
    
]