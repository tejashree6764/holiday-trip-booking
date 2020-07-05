from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
 
 path('',views.index,name='index'),
 path('signup',views.handleSignup,name='handleSignup'),
 path('login',views.handleLogin,name='handleLogin'),
 path('logout',views.handleLogout,name='handleLogout'),
 path('home',views.home,name='home'),
 path('contact',views.contact,name='contact'),
 path('about',views.about,name='about'),
 path('registration',views.registration,name='registration'),
 path('handleBlog',views.handleBlog,name='handleBlog'),

]