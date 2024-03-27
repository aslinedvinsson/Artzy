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
    """
    Renders the latest newsletter using the 'newsletter/newsletter.html' template.
    Retrieves the most recent Newsletter instance from the database,
    ordered by creation date in descending order, and renders it along with a
    new SubscriberForm instance for subscription.
    Args:
        request: HttpRequest object.
    Returns:
        HttpResponse object with rendered newsletter page.
    """
    newsletter = Newsletter.objects.all().order_by('-created_on').first()
    return render(
        request,
        "newsletter/newsletter.html", {
                        "newsletter": newsletter,
                        "subscriber_form": SubscriberForm(),
                     },
    )

def subscribe_to_newsletter(request):
    """
    Handles subscription to the newsletter via POST request; renders
    subscription form otherwise. If the request method is POST and the
    submitted form is valid, saves the new subscriber, sends a confirmation
    email, and redirects to the 'home' page. If the form is invalid,
    it displays an error message.
    Args:
        request: HttpRequest object.
    Returns:
        If POST and form is valid, redirects to 'home'. Otherwise, renders
        the subscription form with an errors.
    """
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
    """
    Sends a confirmation email to a new subscriber. Constructs an unsubscribe
    URL, prepares both HTML and plain text versions of the confirmation message,
    and sends an email to the subscriber's email address.
    Args:
        subscriber: Subscriber instance to whom the confirmation email is sent.
        request: HttpRequest object, used to build absolute URIs.
    """
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
    """
    Unsubscribes a subscriber from the newsletter and returns a confirmation
    message. Attempts to find a Subscriber instance by ID and delete it.
    If the subscriber does not exist, returns a 404 response.
    Args:
        request: HttpRequest object.
        subscriber_id: ID of the Subscriber instance to be deleted.
    Returns:
        HttpResponse object with a success message if unsubscribed, or a 404
        response if subscriber does not exist.
    """
    try:
        subscriber = Subscriber.objects.get(id=subscriber_id)
        subscriber.delete()
        return HttpResponse("You have been successfully unsubscribed. If you ever change your mind, just visit artzy.com and join us again! Best regards, Artzy")
    except Subscriber.DoesNotExist:
        return HttpResponse("Invalid request.", status=404)