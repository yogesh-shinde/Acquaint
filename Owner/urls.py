from django.urls import path, include
from .views import *

urlpatterns = [
    path('view/', Owner_View.as_view(), name='view-owner'),
    path('register/', Owner_Register.as_view(), name='register-owner'),
    path('login/', Owner_Login.as_view(), name='login-owner')
]
