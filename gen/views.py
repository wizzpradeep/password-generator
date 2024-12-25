from django.shortcuts import render
from .models import Password

# Create your views here.
def Home(request):
    password_obj = Password.objects.all()
    context = {
        'passwords':password_obj
    }
    return render(request, 'index.html', context)