from django.urls import path
from articles import views


urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('comments/<int:article_pk>/', views.comment_list),
    path('comments/detail/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/likes/', views.likes),
    path('<int:article_pk>/hates/', views.hates),
]