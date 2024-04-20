from django.shortcuts import render
from .models import CustomerProfile, PerformerProfile


def index(request):
    return render(request, 'index.html')


def customer(request):
    cust = CustomerProfile.objects.all()
    data = {'cust': cust}
    return render(request, 'customer.html', data)


def performer(request):
    perf = PerformerProfile.objects.all()
    data = {'perf': perf}
    return render(request, 'performer.html', data)
