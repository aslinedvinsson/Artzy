from django.shortcuts import render
from django.http import JsonResponse
import re
from .models import Newsletter, Subscriber
from django.core.mail import send_mail
from django.conf import settings


def newsletter(request):
    newsletter = Newsletter.objects.all().order_by('-created_on').first()
    return render(
        request,
        "newsletter/newsletter.html", {
                        "newsletter": newsletter,
                     },
    )

def subscribe_to_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get("email", None)
        name = request.POST.get("name", None)
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email, name=name)
            subscriber.save()
            # Send a confirmation mail
            subject = 'Newsletter Subscription'
            message = f'Hello {name}, thanks for subscribing to our newsletter.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            return JsonResponse({'msg': 'Thanks for subscribing!'})
        else:
            return JsonResponse({'msg': 'Email already subscribed!'})
    return render(request, 'index.html')

def validate_email(request):
    email = request.POST.get("email", None)
    if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        return JsonResponse({'msg': 'Invalid Email Address'})
    elif SubscribedUsers.objects.filter(email=email).exists():
        return JsonResponse({'msg': 'Email already exists'})
    else:
        return JsonResponse({'msg': ''})
