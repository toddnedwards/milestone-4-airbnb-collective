from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse, HttpResponse

from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                f"Message from {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}",
                None,
                ['myairbnbcollective@gmail.com'],
            )
            return render(request, 'success.html')
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})

def success(request):
    return render(request, 'success.html')