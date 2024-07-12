from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from bagianVisitor.models import Contact

def logPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('loginPage')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username    
            return redirect('homePageAdmin')
        else:
            messages.error(request, "Invalid Password")
            return redirect('loginPage')

    # Render the login page template (GET request)
    return render(request, 'admin/logpage.html')

def logout_page(request):
    logout(request)
    request.session.flush() 
    return redirect('loginPage')

def sess_login(request):
    if 'username' in request.session:
        return render(request, 'admin/home.html', {'username': request.session['username']})
    else:
        return redirect('loginPage')

@login_required(login_url='loginPage')
def home(request):
    return render(request, 'admin/home.html')

@login_required(login_url='loginPage')
def contactList(request):
    context = {}
    contactList = Contact.objects.all()
    context['contactList'] = contactList
    return render(request, 'admin/contactList.html', context)

def deleteContact(request, slug):
    try:
        Contact.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('contactListPage')

    return redirect('contactListPage')