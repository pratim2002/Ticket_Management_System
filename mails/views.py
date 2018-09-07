from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from ticket_ms import settings


def email(request):
    subject = 'Thank you'
    message = 'Test Message'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['neetyes2@gmail.com',]

    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

    return render(request, 'mails/index.html')
