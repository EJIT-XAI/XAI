from django.contrib import admin
from django.urls import path, include
from . import views

app_name='accounts'
urlpatterns = [
    path('', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/',views.logout_view,name="logout"),
    
]
