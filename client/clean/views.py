<<<<<<< HEAD:clinzed-1-main/clean/views.py
<<<<<<< HEAD

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import UserProfile  
from .forms import CheckoutForm

def homepage(request):
    return render(request, "pages/homepage.html")
=======
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 
 

def homepage(request):
    return render(request,"pages/homepage.html")

>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
<<<<<<< HEAD

        if User.objects.filter(username=username).exists():  
            messages.error(request, "Username already exists!! Please try another username")
            return redirect('homepage')

        if User.objects.filter(email=email).exists(): 
            messages.error(request, "Email already registered to another account!!")
            return redirect('homepage')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Password does not match! ")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha numeric!")
            return redirect('homepage')  

=======
        
        if User.object.filter(username=username):
            messages.error(request, "Username already exists!! Please try another username")
            return redirect('homepage')
        
        if User.object.filter(email=email):
            messages.error(request, "Email already registered to another account!!")
            return redirect('homepage')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        
        if pass1 != pass2:
            messages.error(request, "Password does not match! ")
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha numeric!")
            return redirect('home')
        
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
<<<<<<< HEAD

        
        UserProfile.objects.create(user=myuser)

        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')

=======
        
        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')
        
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
    return render(request, "pages/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
<<<<<<< HEAD
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/homepage.html", {'fname': fname})
        else:
            messages.error(request, "Wrong password or username!")
            return redirect('homepage')

=======
        user = authenticate(username=username, password=pass1)  
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/homepaage.html", {'fname': fname})
            
        else:
            messages.error(request, "Wrong password or username!")
            return redirect('homepage')
            
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
    return render(request, "pages/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('homepage')
<<<<<<< HEAD

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout_success')
        else:
            form = CheckoutForm()
            
        return render(render, 'checkout.html', {'form': form})

=======
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
=======

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import UserProfile  
from .forms import CheckoutForm 
 

def homepage(request):
    return render(request,"pages/homepage.html")

def dashboard(request):
    return render(request, "pages/accounts/client/dashboard.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():  
            messages.error(request, "Username already exists!! Please try another username")
            return redirect('signup')

        if User.objects.filter(email=email).exists(): 
            messages.error(request, "Email already registered to another account!!")
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Password does not match! ")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha numeric!")
            return redirect('signup') 
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        
        UserProfile.objects.create(user=myuser)

        messages.success(request, "Your Account has been successfully created.")
        return redirect('dashboard')
        
    return render(request, "pages/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('dashboard')
        else:
            messages.error(request, "Wrong password or username!")
            return redirect('signup')
            
    return render(request, "pages/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('homepage')

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout_success')
        else:
            form = CheckoutForm()
            
        return render(render, 'checkout.html', {'form': form})


>>>>>>> 5d934d5 (Legcay dev):client/clean/views.py
