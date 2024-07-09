from django import forms
from django.forms import ModelForm
from .models import Date

from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

class DateInput(forms.DateInput):
    input_type = "date"

class DateForm(forms.ModelForm):

    class Meta:
        model = Date
        fields = ['start_date', 'end_date']
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput()
        }
