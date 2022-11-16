from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from accounts import views

urlpatterns = [
    path('users/', views.users),
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('myprofile/', views.my_profile),
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),
    path('info/', views.users_info),
    path('<username>/', views.profile),
]