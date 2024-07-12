from django.shortcuts import render, redirect
from django.contrib import messages
from bagianVisitor.forms import contactForm
from .models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'visit/index.html')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactPage')  
    else:
        form = contactForm()
    return render(request, 'visit/contact.html', {'form': form})

def payment(request):
    return render(request, 'visit/payment.html')\

def service(request):
    return render(request, 'visit/service.html')

@login_required(login_url='loginPage')
def home(request):
    return render(request, 'admin/home.html')

@login_required(login_url='loginPage')
def contactList(request):
    context = {}
    contactList = Contact.objects.all()
    context['contacList'] = contactList
    return render(request, 'admin/contactList.html', context)