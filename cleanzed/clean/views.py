

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.
def homepage(request):
    return render(request, 'pages/homepage.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['']
        fname = request.POST['']
        lname = request.POSt['']
        email = request.POSt['']
        pass1 = request.POST['']
        pass2 = request.POST['']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "Your Account has been successfully created.")
        
        return redirect('signin')
        
        
    return render(request,"pages/signup.html")

def signin(request):
    
    if request.methode == 'POST':
        username = request.POST['']
        pass1 = request.POST['']
        user = _authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request,user)
        else:
            messages.error(request, "wrong password or username!")
            return redirect('home')
            
    return render(request,"pages/signin.html")


def signout(request):
     logout(request)
     messages.success(request, "logged OUt Successfully!")
     return redirect('homepage')
