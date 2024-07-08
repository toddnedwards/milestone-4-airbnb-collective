from django.shortcuts import render

from .models import Faqs

# Create your views here.

def faqs(request):

    faqs = Faqs.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs.html', context)