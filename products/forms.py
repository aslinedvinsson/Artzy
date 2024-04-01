from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


# Code from Code Institute Boutique Ado Walksthrough
class ProductForm(forms.ModelForm):
    """
    A form for creating or updating Product instances. The form generates
    category choices from the Category model and applies a custom widget to the
    'image' field for file input handling.
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
