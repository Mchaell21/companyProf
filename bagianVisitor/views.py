from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'visit/index.html')

def contact(request):
    return render(request, 'visit/contact.html')

def payment(request):
    return render(request, 'visit/payment.html')\

def service(request):
    return render(request, 'visit/service.html')