from django.shortcuts import render

# Create your views here.
def user_profile(request):

    return render(request, 'my_bookings.html')

