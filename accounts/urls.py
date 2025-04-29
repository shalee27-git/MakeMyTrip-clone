from django.urls import path
from accounts import views
from .views import send_otp

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('register/', views.register, name="register"),
    path('send_otp/<str:email>/', views.send_otp, name="send_otp"),
    path('verifyotp/<str:email>/', views.verify_otp, name="verify-otp"),
    path('verify-account/<token>', views.verify_email_token, name="verify_email_token"),

    path('verifyotp/<str:email>/', views.verify_otp, name="verify-otp"),
    path('login-vendor/', views.login_vendor, name="login_vendor"),
    path('register-vendor/', views.register_vendor, name="register_vendor"),


    path('dashboard/', views.dashboard, name="dashboard"),
    



]