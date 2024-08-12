from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Contact
from user_profile.models import UserProfile

# Create your views here.

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact form data to the database
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )

            # Send email notification
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

    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            form = ContactForm(initial={
                'email': user_profile.user.email,
            })
        except UserProfile.DoesNotExist:
            pass 

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')
