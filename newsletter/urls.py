from django.urls import path
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('subscribe/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('unsubscribe/<int:subscriber_id>/', views.unsubscribe, name='unsubscribe'),
]

