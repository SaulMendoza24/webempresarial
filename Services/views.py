from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    Services = Service.objects.all()
    return render(request,'Services/services.html',{'Services':Services})