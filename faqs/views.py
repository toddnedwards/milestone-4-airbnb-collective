from django.shortcuts import render

from .models import Faq

# Create your views here.


def faqs(request):

    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs.html', context)
