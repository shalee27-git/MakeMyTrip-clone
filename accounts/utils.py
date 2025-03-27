import uuid
from django.core.mail import send_mail
from django.conf import settings



def generateRandomToken():
    return str(uuid.uuid4())


def sendEmailToken(email, token):
    subject = "Verify your email address"
    message = f"""Hi Please verify your email account by clicking this link
    
    http://127.0.0.1:8000/accounts/register/{token}
    
    
    
    """



    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)
    
def sendOTPtoEmail(email, otp):
    subject = "OTP for Account Login"
    message = f"""Hi, use this otp for login
    
      <b>  {otp}</b>
    
    
    
    """



    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)

