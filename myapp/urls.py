from django.urls import path
from myapp import views
from django.contrib import admin
urlpatterns = [
    path('admin_login/',views.ad_login,name='admin_login'),
    path('create_user/',views.create_user,name='create_user'),
    path('user_login/',views.user_login,name='user_login'),
    path('admin_page/',views.admin_page,name='admin_page'),
    path('user_list/',views.user_list,name='user_list'),
]
