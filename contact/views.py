from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse, HttpResponse

from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email
            send_mail(
                f'From {name}, Subject: {subject}',
                f'Message: {message}\nContact Phone: {phone}',
                email,  # From email
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')