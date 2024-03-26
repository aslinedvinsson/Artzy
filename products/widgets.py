from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

# Code from Code Institute Boutique Ado Walksthrough
class CustomClearableFileInput(ClearableFileInput):
    """
    A custom widget for clearable file input with custom template.
    Attributes:
        clear_checkbox_label (str): Label for the clear checkbox. Defaults
        to 'Remove'.
        initial_text (str): Text to display when there is an initial value.
        Defaults to 'Current Image'.
        input_text (str): Text to display as input text, can be empty.
        Defaults to ''.
        template_name (str): Path to the custom widget template.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'