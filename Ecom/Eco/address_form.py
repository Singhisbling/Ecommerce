from django import forms
from .models import Address


class Address_form(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=200)

    class Meta:
        model = Address
        fields = ( 'first_name', 'last_name','address' )