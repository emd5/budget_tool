from django.urls import path
from .views import RegisterApiView, UserApiView
from rest_framework.authtoken import views

urlpatterns = [
    path('user/<int:pk>', UserApiView.as_view(), name='user_detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
]
