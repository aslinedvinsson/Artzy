from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('subscribe/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
   ]
