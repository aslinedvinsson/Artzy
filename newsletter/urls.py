from django.urls import path
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('newsletter_management/', views.newsletter_management, name='newsletter_management'),
    path('send-newsletter/', views.send_newsletter, name='send_newsletter'),
    path('subscribe/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('unsubscribe/<uuid:subscriber_id>/', views.unsubscribe, name='unsubscribe'),
]
