from django.shortcuts import render, redirect
from .models import HotelUser
from django.db.models import Q
from django.contrib import messages
from .utils import generateRandomToken, sendEmailToken, sendOTPtoEmail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import random
from urllib.parse import quote

# Create your views here.
def login(request):

    


    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        hotel_user = HotelUser.objects.filter(
            email = email
        )

        if not hotel_user.exists():
            messages.warning(request, "No Account Found.")
            return redirect('/accounts/login/')
        
        if not hotel_user[0].is_verified:
            messages.warning(request, "Account not verified")
            return redirect('/accounts/login/')




        hotel_user = authenticate(username = hotel_user[0].username, password=password)

        if hotel_user:
            messages.success(request, "Login Success")
            login(request, hotel_user)
            return redirect('/accounts/login/')
        
        messages.warning(request, "Invalid Credentials")
        return redirect('/accounts/login/')


    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
    
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        hotel_user = HotelUser.objects.filter(
            Q(email = email) | Q(phone_number = phone_number)
        )

        if hotel_user.exists():
            messages.warning(request, "Account Exists with this Email or Phone number.")
            return redirect('/accounts/register/')


        hotel_user = HotelUser.objects.create(
            username = phone_number,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            email_token = generateRandomToken()
        )
        hotel_user.set_password(password)
        hotel_user.save()

        sendEmailToken(email, hotel_user.email_token)


        messages.success(request, "An email has been sent to you.")
        return redirect('/accounts/register/')


    return render(request, 'register.html')

def verify_email_token(request, token):
    try:
        hotel_user = HotelUser.objects.get(email_token = token)
        hotel_user.is_verified = True
        hotel_user.save()
        messages.success(request, "Email verified")
        return redirect('/accounts/login/')

    except HotelUser.DoesNotExist:
        return HttpResponse("Invalid Token")
    

def send_otp(request, email):
    try:
        hotel_User = HotelUser.objects.get(email=email)
    except HotelUser.DoesNotExist:
        messages.warning(request, "No account found.")
        return redirect('/accounts/login/')

    otp = random.randint(1000, 9999)  # Generate a 4-digit OTP
    hotel_User.otp = otp  # Save OTP to user model
    hotel_User.save(update_fields=['otp'])  # Ensure OTP is updated

    sendOTPtoEmail(email, otp)  # Send OTP to user's email
    messages.success(request, "OTP has been sent to your email.")
    return redirect(f'/accounts/verifyotp/{email}/')

def verify_otp(request, email):
    if request.method == "POST":
        otp = request.POST.get('otp')

        # Check if user exists
        try:
            hotel_User = HotelUser.objects.get(email=email)
        except HotelUser.DoesNotExist:
            messages.warning(request, "No account found with this email.")
            return redirect('/accounts/login/')

        # Ensure OTP is an integer before comparing
        if otp and otp.isdigit() and int(otp) == hotel_User.otp:
            messages.success(request, "Login Success")
            login(request, hotel_User)
            return redirect('/')

        messages.warning(request, "Wrong OTP")
        return redirect(f'/accounts/verifyotp/{email}/')

    return render(request, 'verifyotp.html')

