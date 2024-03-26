from django.contrib import admin
from .models import UserProfile

# Code from Code Institute Boutique Ado Walksthrough
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin view for UserProfiles.
    """
    list_display = (
        'user', 'default_country'
    )

    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
