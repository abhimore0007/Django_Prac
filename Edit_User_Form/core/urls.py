from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.signup,name='signup'),
    path('login/',views.User_login,name="Login"),
    path('Profile/',views.User_Profile,name="Profile"),
    path('logout/',views.User_logout,name="logout"),
    path('pcf/',views.PCF,name="pcf"),
    path('spf/',views.SPF,name="spf")
]
