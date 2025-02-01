from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tweet import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('delete/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
    
] 
