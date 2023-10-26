from django.urls import path, re_path

from . import views

urlpatterns = [
    path('',views.index,name=""),
    path('sendOTP',views.sendOTP,name="sendOTP"),
    path('verifyemail',views.verifyemail,name="verifyemail"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('signupwithemail',views.signupwithemail,name="signupwithemail")

]