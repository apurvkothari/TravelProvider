from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
from django.core.mail import send_mail


def sent_otp_email(email):
    subject = 'Your account verification email is '
    print(subject)
    otp = random.randint(1000,9999)
    print(otp)
    message = f'The OTP is {otp} '
    print(message)
    email_from = settings.EMAIL_HOST
    print(email_from)
    send_mail(subject, message, email_from, [email], fail_silently=False)
    print('send mail')
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()


