from django import forms

from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)