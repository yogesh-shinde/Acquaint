from django.urls import path, include
from .views import *

urlpatterns = [
    path('view/', User_View.as_view(), name='view-user'),
    path('register/', User_Register.as_view(), name='register-user'),
    path('login/', User_Login.as_view(), name='login-user')
]
