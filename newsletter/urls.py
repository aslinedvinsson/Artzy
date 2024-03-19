from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
    path('newsletter/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('validate_email/', views.validate_email, name='validate_email'),

]
