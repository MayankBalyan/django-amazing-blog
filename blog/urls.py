from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('',home,name="home" ),
    path('blog/<slug:url>/',post,name="post" ),
    path('categories/',categories_page),
    path('categories/<slug:url>/',category),
    path('allposts/',allposts),
    path('about/',about),
    path('login-page/',login_page),
    path('register-page/',register_page),
    path('signup/',handleSignup),
    path('login/', handleLogin),
    path('postComment/', postComment),
    path('logout/',handleLogout)





]
