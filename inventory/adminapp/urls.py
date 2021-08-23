from django.urls import path
from . import views
urlpatterns = [


    path('signup',views.sign_up,name='signup'),
    path('',views.user_login,name='login'),
    path('dashboard',views.user_profile,name='dashboard'),
    path('logout',views.user_logout,name='logout'),
    path('setpassword', views.set_password, name='setpassword'),
]