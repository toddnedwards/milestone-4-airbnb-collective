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
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )

            send_mail(
                subject=(
                    f'Contact Form Submission from '
                    f'{form.cleaned_data["name"]}'
                ),
                message=(
                    f'Name: {form.cleaned_data["name"]}\n'
                    f'Email: {form.cleaned_data["email"]}\n\n'
                    f'Message:\n{form.cleaned_data["message"]}'
                ),
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')
