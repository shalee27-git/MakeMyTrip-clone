from django.urls import path
from . import views
from .views import send_otp

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register_page, name="register"),
    path('send_otp/<str:email>/', views.send_otp, name="send_otp"),
    path('verifyotp/<email>/', views.verify_otp, name="verify_otp"),
    path('verify-accounts/<token>', views.verify_email_token, name="verify_email_token"),


]