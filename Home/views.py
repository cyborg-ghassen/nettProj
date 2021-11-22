from django.shortcuts import redirect, render

from Home.models import User

# Create your views here.
def homePage(request):
    return render(request, 'home/home.html', {})