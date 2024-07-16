from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return HttpResponse('success!')