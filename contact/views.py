from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')
