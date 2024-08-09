from django import forms
from django.forms import ModelForm
from .models import Date

from .models import Property


class PropertyForm(forms.ModelForm):

    guest_count = forms.ChoiceField(
        label='Guest Count', choices=[(i, i) for i in range(1, 20)])

    class Meta:
        model = Property
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)


class DateRangeInput(forms.DateInput):
    input_type = "text"


class DateForm(forms.ModelForm):

    class Meta:
        model = Date
        fields = ['date_range']
        widgets = {
            'date_range': DateRangeInput()
        }
