from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name="base"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.log_out, name="logout"),
    path('Profile/',views.User_Profile, name="Profile")
]
