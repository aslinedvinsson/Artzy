from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
      Attributes:
        list_display: Defines the columns that should be displayed in the admin
        list view.
        fields: Specifies the fields for
        editing.
    """
    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for show and managing ContactRequest message content and
    read status.

    Attributes:
        list_display: Specifies the fields to be displayed in the admin list
        view.
    """

    list_display = ('message', 'read',)
