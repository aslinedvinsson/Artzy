from django.contrib import admin
from .models import Subscriber, Newsletter


class SubscriberAdmin(admin.ModelAdmin):
    """
    Administration for Subscriber models.
     - fields to be displayed in list view
     - order of fields in list view
    """
    list_display = (
        'email', 'name'
    )

    ordering = ('name',)

class NewsletterAdmin(admin.ModelAdmin):
    """
    Administration for Newsletter models.
    - fields to be displayed in list view
    - order of fields in list view
    """
    list_display = (
        'title',
        'created_on',
    )
    ordering = ('-created_on',)

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)