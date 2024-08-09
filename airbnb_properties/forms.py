from django import forms
from django.forms import ModelForm
from .models import Date

from .models import Property


class PropertyForm(forms.ModelForm):

    guest_count = forms.ChoiceField(
        label='Guest Count', choices=[(i, i) for i in range(1, 20)])

    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)

        placeholders = {
            'category': 'Category',
            'name': 'Name',
            'location': 'Location',
            'description': 'Short Description',
            'full_description': 'Full Description',
            'price_per_night': 'Price Per Night (£)',
            'distance_to_airport': 'Distance To Airport (Miles)',
            'bedrooms': 'Number Of Bedrooms',
            'has_wifi': 'Has Wifi',
            'has_parking': 'Has Parking',
            'non_smoking': 'Non Smoking',
            'pet_friendly': 'Pet Friendly',
            'image': 'Main Image',
            'image_kitchen': 'Image Kitchen',
            'image_bathroom': 'Image Bathroom',
            'total_day': 'Total Days',
        }

        for field_name, field in self.fields.items():
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]


class DateRangeInput(forms.DateInput):
    input_type = "text"


class DateForm(forms.ModelForm):

    class Meta:
        model = Date
        fields = ['date_range']
        widgets = {
            'date_range': DateRangeInput()
        }
