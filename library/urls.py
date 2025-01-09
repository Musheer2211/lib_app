from django.contrib import admin
from django.urls import path,include
from views import *

urlpatterns = [
    path('',home_page),
    path('/login',log_in,name='login'),
    path('/books',user_logged_in,name='books')
]