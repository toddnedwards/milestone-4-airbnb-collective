from django import forms
from .models import BookingOrder


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingOrder
        fields = ('first_name', 'last_name', 'email', 'phone_number', 
                  'street_address1', 'street_address2', 'town_or_city', 
                  'county', 'postcode', 'country',)

        def __init__(self, *args, **kwargs):
            """ Remove auto generated labels and set autofocus 
            on first field. Add placeholders
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'first_name' : 'First Name',
                'last_name' : 'Last Name',
                'email': 'Email Address',
                'phone_number': 'Phone Number',
                'street_address1': 'Street Address 1',
                'street_address2': 'Street Address 2',
                'town_or_city': 'Town Or City',
                'county': 'County',
                'postcode': 'Postcode',
                'country': 'Country',        
            }

            """ Creates autofocus on 'first name' form box """
            self.fields['first_name'].widget.attrs['autofocus'] = True
            for field in self.fields:
                if field != 'country':
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
                    