
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Pickup, UserSubscription, UserProfile, Checkout
from .forms import CheckoutForm, PickupForm
from django.utils import timezone
from datetime import timedelta
def homepage(request):
    return render(request, "pages/homepage.html")

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

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        
        UserProfile.objects.create(user=myuser)

        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')

    return render(request, "pages/signup.html")
def subription(request):
    user = request.user
    if UserSubscription.objects.filter(user=user).exists():
        return render(request,'subcription_already_exists.html')
    subscription_start_date = timezone.now()
    subscription_end_date = subscription_start_date + timedelta(weeks=1)
    
    subscription = UserSubscription.objects.create(
        user=user,
        subscription_start_date=subscription_start_date,
        subscription_end_date=subscription_end_date
    
    )
    return render(render, 'subscription_success.html', {'subscription': subscription})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/homepage.html", {'fname': fname})
        else:
            messages.error(request, "Wrong password or username!")
            return redirect('homepage')

    return render(request, "pages/signin.html")

def create_Pickup(request):
    if request.methode == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pickup_list')
    else:
        form = PickupForm()
            
    return render(request, 'create_pickup_html', {'pickeup': Pickup})   

def pickup_list(request):
    pickup = Pickup.objects.all()
    return render(request, 'pickup_list.html', {'pickup': pickup})

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('homepage')

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            
            
            checkout_instance = Checkout(name=name, address=address, phone_number=phone_number, email=email)
            checkout_instance.save()
            return redirect('checkout_success')
        else:
            form = CheckoutForm()
            
        return render(render, 'checkout.html', {'form': form})
