from django.contrib import admin
from .models import Subscriber, Newsletter

# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'name'
    )

    ordering = ('name',)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_on',
    )

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)