from . import  views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('form/',views.form,name='form'),
    path('formfill/', views.formfill, name='formfill'),


]