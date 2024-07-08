from django.contrib import admin
from .models import Faq

# Register your models here.

class FrequentyAskedQuestions(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )

admin.site.register(Faq, FrequentyAskedQuestions)