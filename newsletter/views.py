from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.http import HttpResponse
import re
from .models import Newsletter, Subscriber
from .forms import SubscriberForm



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
            send_confirmation_email(subscriber, request)
            subject = 'Newsletter Subscription'
            messages.success(request, 'Thanks for subscribing!')
            return redirect('home')
        else:
            if 'email' in form.errors:
                messages.error(request, 'Email already subscribed or invalid!')
    else:
        form = SubscriberForm()

    return render(request, 'newsletter/newsletter.html', {'subscriber_form': form})

def send_confirmation_email(subscriber, request):
    unsubscribe_url = request.build_absolute_uri(reverse('newsletter:unsubscribe', args=[subscriber.id]))
    context = {
        'unsubscribe_url': unsubscribe_url,
        'subscriber': subscriber,
    }
    html_message = render_to_string('newsletter/confirmation_newsletter.html', context)
    plain_message = strip_tags(html_message)
    send_mail(
        'Newsletter Subscription',
        plain_message,
        'info@artzy.com',
        [subscriber.email],
        html_message=html_message,
        fail_silently=False,
    )

def unsubscribe(request, subscriber_id):
    try:
        subscriber = Subscriber.objects.get(id=subscriber_id)
        subscriber.delete()
        return HttpResponse("You have been successfully unsubscribed. If you ever change your mind, just visit artzy.com and join us again! Best regards, Artzy")
    except Subscriber.DoesNotExist:
        return HttpResponse("Invalid request.", status=404)