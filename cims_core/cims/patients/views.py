from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'users/patients.html')

def appointments(request):
    return render(request, 'users/appointments.html')

def diagnosis(request):
    return render(request, 'users/diagnosis.html')

def treatment(request):
    return render(request, 'users/treatment.html')