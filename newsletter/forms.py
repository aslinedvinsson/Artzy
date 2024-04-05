from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Subscriber, Newsletter


class SubscriberForm(forms.ModelForm):
    """
    A form for creating a new Subscriber. Initializes fields with custom
    placeholders, classes, and sets autofocus on the first field. Removes
    auto-generated labels for a cleaner UI.
    """
    class Meta:
        model = Subscriber
        fields = ('name', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border-black profile-form-input'
            self.fields[field].label = False



class UnsubscribeForm(forms.Form):
    """
    A form for unsubscribing from the newsletter. Requests email address and
    confirmation to unsubscribe, ensuring user intent.
    """
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'id': 'unsubscribe_email',
            'class': 'border-black profile-form-input',
            'placeholder': 'Email Address *',
        })
    )
    confirm_unsubscribe = forms.BooleanField(
        label='Confirm Unsubscribe',
        widget=forms.CheckboxInput(attrs={
            'id': 'confirm_unsubscribe',
            'class': 'custom-checkbox'
        })
    )


class CreateNewsletterForm(forms.ModelForm):
    """
    A form for creating a new Newsletter. It includes a rich text editor field
    for the newsletter's content via SummernoteWidget, and fields for the
    newsletter's title and associated image.
    """
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Newsletter
        fields = ['title', 'content', 'newsletter_image']


class SendNewsletterForm(forms.Form):
    """
    A form for selecting a Newsletter to send. Lists all available newsletters
    for selection.
    """
    newsletter = forms.ModelChoiceField(queryset=Newsletter.objects.all(),
                                        label="Select Newsletter")
