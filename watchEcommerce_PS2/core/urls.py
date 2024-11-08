from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name="base"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.log_out, name="logout"),
    path('Profile/',views.User_Profile, name="Profile"),
    path('ChangePassword/',views.User_Change_Password, name="changePassword"),
    path('Forgot_Password/',views.User_Password_forgot_Form, name="ForgotPassword"),
    path('categories/',views.User_categories, name="categories"),
    path('watch_details/',views.watch_details, name="watchdetails"),
   
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)