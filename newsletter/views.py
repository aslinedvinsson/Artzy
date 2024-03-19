from django.shortcuts import render, redirect
from django.contrib import messages
import re
from .models import Newsletter, Subscriber
from .forms import SubscriberForm
from django.core.mail import send_mail
from django.conf import settings


def newsletter(request):
    newsletter = Newsletter.objects.all().order_by('-created_on').first()
    return render(
        request,
        "newsletter/newsletter.html", {
                        "newsletter": newsletter,
                        "subscriber_form": SubscriberForm(),
                     },
    )

def subscribe_to_newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            subject = 'Newsletter Subscription'
            message = f'Hello {subscriber.name}, thanks for subscribing to our newsletter.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [subscriber.email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Thanks for subscribing!')
            return redirect('subscribe_to_newsletter')
        else:
            if 'email' in form.errors:
                messages.error(request, 'Email already subscribed or invalid!')
    else:
        form = SubscriberForm()

    return render(request, 'newsletter/newsletter.html', {'subscriber_form': form})