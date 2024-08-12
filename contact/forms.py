from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Email Address"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Name"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your Message"})
    )
