from django.urls import path, include
from .views import *

urlpatterns = [
    path('view/', Admin_View.as_view(), name='view'),
    path('register/', Admin_Register.as_view(), name='register'),
    path('login/', Admin_Login.as_view(), name='login')
]
