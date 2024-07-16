from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    email = forms.CharField(validators=[EmailValidator()])
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)